'use strict';
// Deterministic 50fps capture of a scripted UI interaction. Same stepped-time model as
// capture-site.cjs: every frame advances page time by exactly 20ms.
// usage: node capture-timeline.cjs <spec.json> <outDir>
// spec: { url, viewport: "1280x800", duration: s, settle: ms,
//         actions: [{ t: s, click: css, hasText?: str } | { t, mouse: [x, y] } | { t, scroll: y }] }
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [specPath, outDir] = process.argv.slice(2);
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const FPS = 50;
const DT = 1000 / FPS;
const [VW, VH] = (spec.viewport || '1280x800').split('x').map(Number);
const frames = Math.round(spec.duration * FPS);
const due = new Map();
for (const a of spec.actions) {
  const i = Math.round(a.t * FPS);
  due.set(i, [...(due.get(i) || []), a]);
}

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({ args: ['--use-angle=metal', '--hide-scrollbars', '--force-color-profile=srgb'] });
  const context = await browser.newContext({ viewport: { width: VW, height: VH }, deviceScaleFactor: 1 });
  const page = await context.newPage();
  await page.clock.install();
  await page.goto(spec.url, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(spec.settle ?? 1500);
  await page.mouse.move(VW - 2, VH - 2);

  await page.evaluate(() => {
    const seen = new WeakSet();
    const step = (dt, adopt) => {
      for (const a of document.getAnimations()) {
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
    window.__step = (dt) => step(dt, false);
  });
  const fakeNow = await page.evaluate(() => Date.now());
  await page.clock.pauseAt(fakeNow + 100);
  await page.evaluate(() => window.__adopt());

  const log = [];
  for (let i = 0; i < frames; i++) {
    for (const a of due.get(i) || []) {
      if (a.click) {
        let loc = page.locator(a.click);
        if (a.hasText) loc = loc.filter({ hasText: a.hasText });
        await loc.first().click({ timeout: 5000 });
      } else if (a.mouse) {
        await page.mouse.move(a.mouse[0], a.mouse[1]);
      } else if ('scroll' in a) {
        await page.evaluate((y) => window.scrollTo({ top: y, behavior: 'instant' }), a.scroll);
      }
      log.push({ i, action: a });
    }
    await page.waitForTimeout(20);
    await page.clock.runFor(DT);
    await page.evaluate((dt) => window.__step(dt), DT);
    await page.screenshot({ path: path.join(outDir, `f-${String(i).padStart(4, '0')}.png`) });
  }
  fs.writeFileSync(path.join(outDir, 'frames.json'), JSON.stringify({ spec, fps: FPS, frames, log }, null, 1));
  console.log(`${spec.url}: ${frames} frames, ${log.length} actions`);
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
