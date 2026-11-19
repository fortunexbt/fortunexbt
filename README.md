<a href="https://fortunexbt.com"><picture><source media="(prefers-color-scheme: dark)" srcset="./art/masthead-dark.svg"><img src="./art/masthead-light.svg" alt="fortunexbt, wearing a pair of Pit Viper sunglasses" width="100%"></picture></a>

I build software you can run today. Control planes that stop an agent when you say stop, a trading desk that audits itself, Mac and data tools that keep everything local, and games for the browser and the terminal.

[fortunexbt.com](https://fortunexbt.com) · [X](https://x.com/fortunexbt) · [Telegram](https://t.me/fortunexbt) · [Exit Node](https://fortunexbt.substack.com/)

<picture><source media="(prefers-color-scheme: dark)" srcset="./art/start-here-dark.svg"><img src="./art/start-here-light.svg" alt="Start here" width="100%"></picture>

<table><tr>
<td width="58%" valign="top"><a href="https://github.com/mutx-dev/mutx-dev"><img src="./assets/mutx.gif" alt="MUTX dashboard: an operator pauses an agent session and resumes it" /></a></td>
<td width="42%" valign="top"><h3><a href="https://github.com/mutx-dev/mutx-dev">MUTX</a></h3>A control plane for AI agents. Operators deploy agents, watch every run, set budgets and approval rules, and stop any run. FastAPI, Next.js, a macOS app, a CLI and a Python SDK, built in the open by me and my agents.<br><br><a href="https://docs.mutx.dev/">Docs</a> · <a href="https://github.com/mutx-dev/mutx-dev">Code</a></td>
</tr></table>

<table><tr>
<td width="42%" valign="top"><h3><a href="https://github.com/archonHL/archon">Archon</a></h3>A trading desk on Hyperliquid that improves itself. Agents propose strategies around the clock, and one evaluator tests each on prices it was never tuned on. A strategy is listed only if it beats holding the same markets. Every step is a line in a hash-chained record, and the verifier that checks it is public, dependency-free Python.<br><br><a href="https://archon.quest/">Site</a> · <a href="https://github.com/archonHL/archon">Code</a></td>
<td width="58%" valign="top"><a href="https://archon.quest/"><img src="./assets/archon.gif" alt="Archon's desk page: a shortlist of listed strategies, each charted against holding the same markets" /></a></td>
</tr></table>

<table><tr>
<td width="58%" valign="top"><a href="https://github.com/fortunexbt/bollard"><img src="./assets/bollard.png" alt="Bollard menu bar panel listing local servers and background jobs by project, branch and the agent that started each" /></a></td>
<td width="42%" valign="top"><h3><a href="https://github.com/fortunexbt/bollard">Bollard</a></h3>Everything you left running on your Mac, in the menu bar. Servers, scripts, background jobs and agent sessions, each named by project and git branch, with who started it and a Stop button that works. Agents can find and stop things too, through a built-in MCP server.<br><br><code>brew trust --cask fortunexbt/tap/bollard</code><br><code>brew install --cask fortunexbt/tap/bollard</code><br><br><a href="https://github.com/fortunexbt/bollard">Code</a> · <a href="https://github.com/fortunexbt/bollard/releases">Releases</a></td>
</tr></table>

<picture><source media="(prefers-color-scheme: dark)" srcset="./art/agent-controls-dark.svg"><img src="./art/agent-controls-light.svg" alt="Agent controls" width="100%"></picture>

Does the agent stop when told, stay under budget and wait for approval? These test it, gate it and write the receipt.

<table>
<tr>
<td width="33%" valign="top">
<a href="https://fortunexbt.github.io/boundary-bench/"><img src="./assets/boundary-bench.gif" alt="BoundaryBench report replaying agent runs against budget, stop and approval controls" /></a>
<br><b><a href="https://github.com/fortunexbt/boundary-bench">BoundaryBench</a></b>
<br>Crash tests for agent controls. Every tool call is a block, the boundary is a wall, and anything past it shows red.
<br><a href="https://fortunexbt.github.io/boundary-bench/">Report</a> · <a href="https://github.com/fortunexbt/boundary-bench">Code</a>
</td>
<td width="33%" valign="top">
<a href="https://switchyard-phi.vercel.app/"><img src="./assets/switchyard.gif" alt="Switchyard console replaying an incident drill through a policy gate, stopped mid-run, with a receipt in the ledger" /></a>
<br><b><a href="https://github.com/fortunexbt/switchyard">Switchyard</a></b>
<br>A policy gate, a stop and a hash-only receipt for the tools an agent calls. Press Replay, then Stop.
<br><a href="https://switchyard-phi.vercel.app/">Try it</a> · <a href="https://github.com/fortunexbt/switchyard">Code</a>
</td>
<td width="33%" valign="top">
<a href="https://ambient-relay.vercel.app/"><img src="./assets/ambient-relay.gif" alt="Ambient Relay routing a synthetic Discord stream through a policy, one decision per event" /></a>
<br><b><a href="https://github.com/fortunexbt/ambient-relay">Ambient Relay</a></b>
<br>A Discord automation lab that proves the dangerous part first. Which event triggers which reply, without sending anything.
<br><a href="https://ambient-relay.vercel.app/">Try it</a> · <a href="https://github.com/fortunexbt/ambient-relay">Code</a>
</td>
</tr>
</table>

<picture><source media="(prefers-color-scheme: dark)" srcset="./art/local-first-tools-dark.svg"><img src="./art/local-first-tools-light.svg" alt="Local-first tools" width="100%"></picture>

They run on your machine, on your files, and show the rows, the drawing or the public record behind every answer.

<table>
<tr>
<td width="25%" valign="top">
<a href="https://tablebeam-eight.vercel.app/"><img src="./assets/tablebeam.gif" alt="Tablebeam answering a spreadsheet question with an exact figure and the rows it used" /></a>
<br><b><a href="https://github.com/fortunexbt/tablebeam">Tablebeam</a></b>
<br>Ask a spreadsheet a question and get the exact answer with the rows it used. Exact decimals, no model required.
<br><a href="https://tablebeam-eight.vercel.app/">Try it</a> · <a href="https://github.com/fortunexbt/tablebeam">Code</a>
</td>
<td width="25%" valign="top">
<a href="https://fieldwork-plugins.vercel.app/"><img src="./assets/fieldwork.gif" alt="Fieldwork catalog running one of its eight tools in the browser" /></a>
<br><b><a href="https://github.com/fortunexbt/fieldwork-plugins">Fieldwork plugins</a></b>
<br>Eight small plugins for ChatGPT and Codex. The catalog runs the same scripts in your browser on real public data.
<br><a href="https://fieldwork-plugins.vercel.app/">Try it</a> · <a href="https://github.com/fortunexbt/fieldwork-plugins">Code</a>
</td>
<td width="25%" valign="top">
<a href="https://github.com/fortunexbt/world-watch"><img src="./assets/world-watch.gif" alt="World Watch map of live earthquakes, alerts and fires, each linked to its public source" /></a>
<br><b><a href="https://github.com/fortunexbt/world-watch">World Watch</a></b>
<br>Earthquakes, alerts, storms and fires on one live map, every marker linked to its public record.
<br><a href="https://github.com/fortunexbt/world-watch">Code</a>
</td>
<td width="25%" valign="top">
<a href="https://render-studio-delta.vercel.app/"><img src="./assets/render-studio.gif" alt="Render Studio selecting an area of an archive plan and producing a plan view of it" /></a>
<br><b><a href="https://render-studio-delta.vercel.app/">Render Studio</a></b>
<br>An Italian workspace for architects. Mark an area of a drawing and develop views from it.
<br><a href="https://render-studio-delta.vercel.app/">Try it</a>
</td>
</tr>
</table>

<picture><source media="(prefers-color-scheme: dark)" srcset="./art/labs-and-benches-dark.svg"><img src="./art/labs-and-benches-light.svg" alt="Labs and benches" width="100%"></picture>

Seeded simulations and paired measurements. The same link or the same command replays the same run.

<table>
<tr>
<td width="33%" valign="top">
<a href="https://queueglass.vercel.app/"><img src="./assets/queueglass.gif" alt="Queueglass simulation of a backlog building at one stage and draining" /></a>
<br><b><a href="https://github.com/fortunexbt/queueglass">Queueglass</a></b>
<br>Watch a queue back up under load and recover. Seeded, so a link replays the exact run.
<br><a href="https://queueglass.vercel.app/">Try it</a> · <a href="https://github.com/fortunexbt/queueglass">Code</a>
</td>
<td width="33%" valign="top">
<a href="https://fortunexbt.github.io/barter/"><img src="./assets/barter.gif" alt="Barter Protocol Lab stepping a commodity exchange through its hash-chained journal" /></a>
<br><b><a href="https://github.com/fortunexbt/barter">Barter</a></b>
<br>A commodity barter state machine on a balance scale, with a hash-chained journal, priced from the World Bank Pink Sheet.
<br><a href="https://fortunexbt.github.io/barter/">Try it</a> · <a href="https://github.com/fortunexbt/barter">Code</a>
</td>
<td width="33%" valign="top">
<a href="https://fortunexbt.github.io/minecraft-apple-silicon-framework/"><img src="./assets/minecraft.gif" alt="Minecraft shader setups for Apple silicon with screenshots and measured results" /></a>
<br><b><a href="https://github.com/fortunexbt/minecraft-apple-silicon-framework">Minecraft on Apple silicon</a></b>
<br>Shader setups for M-series Macs, flown over one scripted route and compared frame by frame, with a CLI that tries one and rolls it back.
<br><a href="https://fortunexbt.github.io/minecraft-apple-silicon-framework/">Browse</a> · <a href="https://github.com/fortunexbt/minecraft-apple-silicon-framework">Code</a>
</td>
</tr>
</table>

<picture><source media="(prefers-color-scheme: dark)" srcset="./art/data-up-close-dark.svg"><img src="./art/data-up-close-light.svg" alt="Data up close" width="100%"></picture>

A writer's rhythm, a funding round, one harrier's year. Each takes real data and makes one thing about it plain.

<table>
<tr>
<td width="33%" valign="top">
<a href="https://ghostwriter-virid-xi.vercel.app/"><img src="./assets/ghostwriter.gif" alt="Ghostwriter charting a writer's sentence rhythm and punctuation beside the manuscript" /></a>
<br><b><a href="https://ghostwriter-virid-xi.vercel.app/">Ghostwriter</a></b>
<br>Paste a writer's posts and see how they write, measured sentence by sentence.
<br><a href="https://ghostwriter-virid-xi.vercel.app/">Try it</a>
</td>
<td width="33%" valign="top">
<a href="https://crypto-hiring-radar.vercel.app/"><img src="./assets/hiring-radar.gif" alt="Hiring Radar showing funding rounds as radar blips with predicted hires and reasoning" /></a>
<br><b><a href="https://crypto-hiring-radar.vercel.app/">Hiring Radar</a></b>
<br>Crypto funding rounds, and the roles each company is likely to hire next, with a reason for every call.
<br><a href="https://crypto-hiring-radar.vercel.app/">Try it</a>
</td>
<td width="33%" valign="top">
<a href="https://bird-migration-chi.vercel.app/"><img src="./assets/fieldguide.gif" alt="Fieldguide replaying a tagged marsh harrier's GPS track from Belgium to Mauritania" /></a>
<br><b><a href="https://bird-migration-chi.vercel.app/">Fieldguide</a></b>
<br>Follow one tagged bird from Flanders. Real GPS tracks, replayed day by day.
<br><a href="https://bird-migration-chi.vercel.app/">Try it</a>
</td>
</tr>
</table>

<picture><source media="(prefers-color-scheme: dark)" srcset="./art/games-dark.svg"><img src="./art/games-light.svg" alt="Games" width="100%"></picture>

<table>
<tr>
<td width="25%" valign="top">
<a href="https://fortunexbt.github.io/solar-drift/"><img src="./assets/solar-drift.gif" alt="Solar Drift gameplay: looping around suns and crossing the wake to capture them" /></a>
<br><b><a href="https://github.com/fortunexbt/solar-drift">Solar Drift</a></b>
<br>Loop around a sun and cross your own wake to capture it.
<br><a href="https://fortunexbt.github.io/solar-drift/">Play</a> · <a href="https://github.com/fortunexbt/solar-drift">Code</a>
</td>
<td width="25%" valign="top">
<a href="https://fortunexbt.github.io/loop-courier/"><img src="./assets/loop-courier.gif" alt="Loop Courier gameplay: drawing a delivery route through a city" /></a>
<br><b><a href="https://github.com/fortunexbt/loop-courier">Loop Courier</a></b>
<br>Draw one route through a seeded night city and make every deadline.
<br><a href="https://fortunexbt.github.io/loop-courier/">Play</a> · <a href="https://github.com/fortunexbt/loop-courier">Code</a>
</td>
<td width="25%" valign="top">
<a href="https://terminal-starfield.vercel.app/"><img src="./assets/terminal-starfield.gif" alt="Terminal Starfield: space combat drawn in terminal characters" /></a>
<br><b><a href="https://github.com/fortunexbt/terminal-starfield">Terminal Starfield</a></b>
<br>A space-combat roguelite for the terminal, in pure Python.
<br><a href="https://terminal-starfield.vercel.app/">Play</a> · <a href="https://github.com/fortunexbt/terminal-starfield">Code</a>
</td>
<td width="25%" valign="top">
<a href="https://ckitty.vercel.app/"><img src="./assets/ckitty.gif" alt="ckitty: a cat drawn in terminal characters changing pose" /></a>
<br><b><a href="https://github.com/fortunexbt/ckitty">ckitty</a></b>
<br>A cat for your terminal, in C. The web build is 65 KB of WebAssembly.
<br><a href="https://ckitty.vercel.app/">Play</a> · <a href="https://github.com/fortunexbt/ckitty">Code</a>
</td>
</tr>
</table>

<picture><source media="(prefers-color-scheme: dark)" srcset="./art/measured-dark.svg"><img src="./art/measured-light.svg" alt="Things I measured" width="100%"></picture>

- pandas, SQLite and DuckDB silently returned wrong totals on 12–17% of real Wikipedia-table questions. Tablebeam returned 0.4%. [Eval](https://github.com/fortunexbt/tablebeam/tree/f141ee739f/eval)
- Claude Code kept calling write tools after the server said the budget was spent, in 5 of 5 runs. [Traces](https://github.com/fortunexbt/boundary-bench/tree/e937412/runs/2026-10-23-claude-code-haiku)
- Coding agents fell into loops of failing tool calls in 8.2% of 7,903 real sessions.
- A published estimate of how many Moltbook agents act on their own did not reproduce on two public crawls.
- A rule-based prompt-injection filter caught 0 of 320 attacks it was not written for.

The data, the limits and the command that reproduces each one are on [fortunexbt.com](https://fortunexbt.com/#findings).

<picture><source media="(prefers-color-scheme: dark)" srcset="./art/upstream-dark.svg"><img src="./art/upstream-light.svg" alt="Upstream and smaller" width="100%"></picture>

- [google/adk-js#952](https://github.com/google/adk-js/pull/952) Merged upstream. The library now requires HTTPS for implicit Google API authentication.
- [silicon-lab](https://github.com/fortunexbt/silicon-lab) Paired A-B-B-A benchmarking on one machine, with bootstrap intervals and three reproducible reports.
- [Minecraft Frame Bench](https://github.com/fortunexbt/minecraft-frame-bench) Frame timing from the real Minecraft Java client over scripted routes, with a guard against the AFK throttle.
- [Flock baseline runner](https://github.com/fortunexbt/flock-baseline-runner) Baseline and A-B-B-A kernel experiments for the public Flock BLAKE3 challenge, on GitHub-hosted runners.
- [Field Manual](https://fortunexbt-docs.vercel.app/) Architecture notes, measured results and reproduction steps for everything above.

<img src="./assets/fortune.webp" alt="Marble bust of Julius Caesar wearing mirrored sport sunglasses" width="96" align="left">

**fortunexbt**<br>
[fortunexbt.com](https://fortunexbt.com) · [X](https://x.com/fortunexbt) · [Telegram](https://t.me/fortunexbt) · [Exit Node](https://fortunexbt.substack.com/)<br>
