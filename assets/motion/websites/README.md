# Website motion captures

Public websites captured with an automated Chromium browser on real GPU rendering. These show the live pages (and, for Antico Frantoio Nunzi, the published redesign proposal). They are not mockups.

Bottega Dei Priori and MUD are shared work with **Walberth Soares** through [Civico Due](https://civicodue.eu/). Keep that credit beside the profile presentation.

| Capture | Site | Duration | GIF frames | Bytes |
| --- | --- | --- | --- | --- |
| [civico-due.gif](./civico-due.gif) | Civico Due | 5.30s | 150 | 627,438 |
| [bottega-priori.gif](./bottega-priori.gif) | Bottega Dei Priori | 4.40s | 169 | 5,240,396 |
| [mud-ceramica.gif](./mud-ceramica.gif) | MUD Escola de Cerâmica | 4.40s | 167 | 5,618,735 |
| [antico-frantoio-nunzi.gif](./antico-frantoio-nunzi.gif) | Antico Frantoio Nunzi (redesign proposal) | 4.40s | 167 | 3,285,798 |
| [victoria-inaudi.gif](./victoria-inaudi.gif) | Victoria Inaudi | 4.40s | 166 | 2,244,506 |
| [elisa-panzavolta.gif](./elisa-panzavolta.gif) | Elisa Panzavolta | 4.40s | 187 | 2,166,426 |

Each clip holds on the homepage, scrolls down on a cubic ease, holds, and scrolls back to the top so the loop has no jump. The viewport is 1280 × 800 at device scale 1, exported at 480 × 300.

Time is stepped, not recorded. Every frame advances the page by exactly 20ms (timers, `requestAnimationFrame`, CSS and Web Animations, video), so frame pacing doesn't depend on how fast the machine renders. GIFs play at 50fps, the fastest delay browsers honour (20ms). Identical consecutive frames are merged into one longer frame by the encoder, which happens during the holds and in pinned scroll sections.

[captures.json](./captures.json) records the source URL, scroll path, frame counts, bytes and SHA-256 for each file. To refresh, recapture all six with the commands in [../capture/README.md](../capture/README.md) so the grid stays consistent.
