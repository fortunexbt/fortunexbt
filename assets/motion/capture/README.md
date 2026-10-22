# Capture scripts

These produce the profile GIFs. Both step page time by exactly 20ms per frame (Playwright's clock for timers, `requestAnimationFrame` and `performance`, plus manual stepping of CSS and Web Animations), so frame pacing doesn't depend on how fast the machine renders. Chromium runs with `--use-angle=metal` so WebGL uses the GPU.

Install Playwright and Chromium once with `npm i playwright && npx playwright install chromium`, plus `brew install gifski gifsicle`.

## Websites

`capture-site.cjs <url> <outDir> <distancePx>` holds on the page, scrolls down on a cubic ease, holds, and scrolls back to the top. Each frame logs its real `scrollY` next to the target, and the script reports any frame more than 1px off.

```sh
T="--holdTop 0.5 --down 2.4 --holdBottom 0.4 --up 1.1"
node capture-site.cjs https://civicodue.eu/ out/civico 2300 --holdTop 0.5 --down 3.0 --holdBottom 0.4 --up 1.4
node capture-site.cjs https://www.bottegapriori.com/ out/bottega 1300 $T
node capture-site.cjs https://mudescoladeceramica.com/pt out/mud 1250 $T
node capture-site.cjs https://antico-frantoio-nunzi.vercel.app/ out/nunzi 1250 $T
node capture-site.cjs https://www.victoriainaudi.com/ out/victoria 1250 $T --dismiss "Seguir en español"
node capture-site.cjs https://elisapanzavolta.com/ out/elisa 1300 $T --dismiss Rifiuta
gifski --fps 50 --width 480 --quality 75 --motion-quality 60 --lossy-quality 60 -o civico-due.gif out/civico/f-*.png
```

## Tool demos

`capture-timeline.cjs <spec.json> <outDir>` runs the clicks in a spec at fixed times. `boundary-bench.json` and `barter.json` expect each project's production build served locally (BoundaryBench at `/boundary-bench/` on port 4319, Barter's `npm run build:pages` output at `/barter/` on port 4173).

```sh
node capture-timeline.cjs boundary-bench.json out/boundary-bench
gifski --fps 50 --width 640 --quality 90 -o boundary-bench.gif out/boundary-bench/f-*.png
```

## Checks before committing

- `gifsicle --info <gif>` shows 0.02s delays on motion frames. Browsers play delays of 0.01s or less at 0.1s, so 50fps is the ceiling.
- Look at a contact sheet of every 12th frame for banners, unloaded images or a stalled animation.
- The first and last frames should match so the loop has no jump.
- Update `captures.json` and `../manifest.json` with bytes and SHA-256.
