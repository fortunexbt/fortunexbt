# Keeping the profile demos current

The current refresh (8 September 2026) includes the local Odyssey and ckitty builds, the latest public Tablebeam banner, and refreshed public snapshots for BoundaryBench, Queueglass and Switchyard. The website recordings were also captured again from the live public pages.

The profile links to the repositories for current builds. These GIFs are snapshots of actual project demos, terminal output or public websites. They are not release or production-status claims.

Keep each project's filename stable when replacing a clip. The README layout can then stay intact as projects change. If a new build changes the purpose or availability of a feature, update its caption and link too.

For a refresh:

1. Use a published build or an isolated checkout of the intended revision. Do not alter another agent's active checkout to make a recording.
2. Record one legible interaction: a successful game move, a query and its source rows, a simulation change, or a useful website section. Use public sample data. Keep credentials, contact addresses and private workspace details out of the frame.
3. Retain the software's actual UI and aspect ratio. Avoid fake browser frames, decorative overlays and invented activity. Label generated fixtures and work-in-progress builds in the caption.
4. Export an animated GIF around 600–800px wide. A short 5–9 second clip is usually enough; keep file size low without turning text or motion into noise.
5. Check the first frame, the interaction, and the repeat boundary. Inspect the rendered README on GitHub at desktop and phone widths.
6. Update the source revision, capture date and method in `manifest.json`.

Existing public project animations may be reused when their provenance is clear. A deterministic terminal rendering is a valid project demo; do not describe it as a live production recording.

This directory has no scheduled capture or automatic publishing process.

## Source credits

Project and source-revision links are recorded per asset in `manifest.json`. The ckitty excerpt reuses the project's published deterministic renderer frames, with framing changes; its GPL-3.0 license is retained in [games/ckitty-LICENSE.txt](./games/ckitty-LICENSE.txt). The complete renderer source is linked by the manifest. Bottega and MUD retain their shared Civico Due credit in the main profile and website capture notes.
