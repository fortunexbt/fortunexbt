'use strict';
// Deterministic 50fps scroll capture: every frame advances page time by exactly 20ms
// (fake clock for timers/rAF, manual stepping for CSS and WAAPI animations), so frame
// pacing never depends on how fast the machine renders or screenshots.
// usage: node capture-site.cjs <url> <outDir> <distance> [--down s] [--up s] [--dismiss text]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [url, outDir, distArg, ...rest] = process.argv.slice(2);
const opt = { down: 2.8, up: 1.4, holdTop: 0.6, holdBottom: 0.5, dismiss: null, settle: 3500, viewport: '1280x800' };
for (let i = 0; i < rest.length; i += 2) {
  const k = rest[i].replace(/^--/, '');
  opt[k] = isNaN(Number(rest[i + 1])) ? rest[i + 1] : Number(rest[i + 1]);
}
const D = Number(distArg);
const FPS = 50;
const DT = 1000 / FPS;
const [VW, VH] = String(opt.viewport).split('x').map(Number);

const ease = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
function scrollAt(t) {
  const a = opt.holdTop, b = a + opt.down, c = b + opt.holdBottom, d = c + opt.up;
  if (t < a) return 0;
  if (t < b) return D * ease((t - a) / opt.down);
  if (t < c) return D;
  if (t < d) return D * (1 - ease((t - c) / opt.up));
  return 0;
}
const total = opt.holdTop + opt.down + opt.holdBottom + opt.up;
const frames = Math.round(total * FPS);

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({
    args: ['--use-angle=metal', '--hide-scrollbars', '--force-color-profile=srgb', '--autoplay-policy=no-user-gesture-required'],
  });
  const context = await browser.newContext({ viewport: { width: VW, height: VH }, deviceScaleFactor: 1 });
  const page = await context.newPage();
  await page.clock.install();
  await page.goto(url, { waitUntil: 'networkidle', timeout: 90000 });
  if (opt.dismiss) {
    const byRole = page.getByRole('button', { name: String(opt.dismiss) }).first();
    const target = (await byRole.count()) ? byRole : page.getByText(String(opt.dismiss), { exact: true }).first();
    await target.click({ timeout: 10000 });
  }
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(opt.settle);

  await page.evaluate(() => {
    const seen = new WeakSet();
    const step = (dt, adopt) => {
      for (const a of document.getAnimations()) {
        // Scroll and view timelines follow scroll position on their own.
        if (a.timeline !== document.timeline) continue;
        if (!seen.has(a)) {
          seen.add(a);
          if (a.playState !== 'running') continue;
          a.pause();
          if (!adopt) a.currentTime = 0;
        }
        if (a.playState === 'paused') a.currentTime = (a.currentTime || 0) + dt;
      }
    };
    window.__adopt = () => step(0, true);
    window.__step = async (dt) => {
      step(dt, false);
      const vids = [...document.querySelectorAll('video')].filter((v) => v.readyState >= 2 && v.duration);
      await Promise.all(vids.map((v) => new Promise((res) => {
        if (!v.paused) v.pause();
        v.addEventListener('seeked', res, { once: true });
        setTimeout(res, 0);
        v.currentTime = (v.currentTime + dt / 1000) % v.duration;
      })));
    };
    window.__imagesReady = async () => {
      const inView = [...document.images].filter((img) => {
        const r = img.getBoundingClientRect();
        return r.bottom > 0 && r.top < innerHeight && r.width > 0;
      });
      await Promise.all(inView.map((img) => (img.complete ? img.decode().catch(() => {}) : new Promise((res) => {
        img.addEventListener('load', res, { once: true });
        img.addEventListener('error', res, { once: true });
      }).then(() => img.decode().catch(() => {})))));
    };
  });
  const fakeNow = await page.evaluate(() => Date.now());
  await page.clock.pauseAt(fakeNow + 100);
  await page.evaluate(() => window.__adopt());

  const log = [];
  for (let i = 0; i < frames; i++) {
    const target = Math.round(scrollAt(i / FPS));
    await page.evaluate((y) => window.scrollTo({ top: y, left: 0, behavior: 'instant' }), target);
    await page.waitForTimeout(25);
    await page.clock.runFor(DT);
    await page.evaluate((dt) => window.__step(dt), DT);
    await Promise.race([page.evaluate(() => window.__imagesReady()), page.waitForTimeout(8000)]);
    const scrollY = await page.evaluate(() => Math.round(scrollY));
    await page.screenshot({ path: path.join(outDir, `f-${String(i).padStart(4, '0')}.png`) });
    log.push({ i, target, scrollY });
  }
  const off = log.filter((f) => Math.abs(f.target - f.scrollY) > 1);
  fs.writeFileSync(path.join(outDir, 'frames.json'), JSON.stringify({ url, fps: FPS, frames, opt, D, log }, null, 1));
  console.log(`${url}: ${frames} frames, ${off.length} frames off target${off.length ? ' e.g. ' + JSON.stringify(off.slice(0, 3)) : ''}`);
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
