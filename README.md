# fortunexbt

I build the software I (and maybe, you) need: an agent control plane, a Mac menu bar app, local-first data & LLM tooling, and games for the browser and the terminal.

<a href="https://github.com/mutx-dev/mutx-dev"><img src="./assets/mutx.gif" width="100%" alt="MUTX dashboard: an operator pauses an agent session and resumes it" /></a>

**[MUTX](https://github.com/mutx-dev/mutx-dev)** is a control plane for AI agents. Operators deploy agents, watch every run, set budgets and approval rules, and stop any run. FastAPI, Next.js, a macOS app, a CLI and a Python SDK: 249 API route handlers and 3,336 tests. [Docs](https://docs.mutx.dev/)

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/fortunexbt/bollard"><img src="./assets/bollard.png" alt="Bollard menu bar panel listing local dev servers with ports, CPU, memory and uptime" /></a>
<br><b><a href="https://github.com/fortunexbt/bollard">Bollard</a></b>
<br>Every server on your Mac in the menu bar, named by project and git branch, with a Stop button that works. SwiftUI and a small C bridge over Darwin's kernel tables.
<br><code>brew install --cask fortunexbt/tap/bollard</code>
</td>
<td width="50%" valign="top">
<a href="https://tablebeam-eight.vercel.app/"><img src="./assets/tablebeam.gif" alt="Tablebeam answering a spreadsheet question with an exact figure and the rows it used" /></a>
<br><b><a href="https://github.com/fortunexbt/tablebeam">Tablebeam</a></b>
<br>Ask a spreadsheet a question and get the exact answer with the rows it used. The arithmetic runs in exact decimals, no model required.
<br><a href="https://tablebeam-eight.vercel.app/">Try it</a> · <a href="https://github.com/fortunexbt/tablebeam">Code</a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://fortunexbt.github.io/boundary-bench/"><img src="./assets/boundary-bench.gif" alt="BoundaryBench report replaying agent runs against budget, stop and approval controls" /></a>
<br><b><a href="https://github.com/fortunexbt/boundary-bench">BoundaryBench</a></b>
<br>Crash tests for agent controls. Does the agent stop when told, stay under budget, wait for approval? The server keeps the score.
<br><a href="https://fortunexbt.github.io/boundary-bench/">Report</a> · <a href="https://github.com/fortunexbt/boundary-bench">Code</a>
</td>
<td width="50%" valign="top">
<a href="https://queueglass.vercel.app/"><img src="./assets/queueglass.gif" alt="Queueglass simulation of a backlog building at one stage and draining" /></a>
<br><b><a href="https://github.com/fortunexbt/queueglass">Queueglass</a></b>
<br>Watch a queue back up under load and recover. Seeded, so a link replays the exact run.
<br><a href="https://queueglass.vercel.app/">Try it</a> · <a href="https://github.com/fortunexbt/queueglass">Code</a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://fortunexbt.github.io/minecraft-apple-silicon-framework/"><img src="./assets/minecraft.gif" alt="The same Minecraft view under three shader setups measured on Apple silicon" /></a>
<br><b><a href="https://github.com/fortunexbt/minecraft-apple-silicon-framework">Minecraft on Apple silicon</a></b>
<br>Shader setups for M-series Macs, each measured over the same scripted flight, with a CLI that tries one and rolls it back.
<br><a href="https://fortunexbt.github.io/minecraft-apple-silicon-framework/">Browse</a> · <a href="https://github.com/fortunexbt/minecraft-apple-silicon-framework">Code</a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/fortunexbt/world-watch"><img src="./assets/world-watch.gif" alt="World Watch map of live earthquakes, alerts and fires, each linked to its public source" /></a>
<br><b><a href="https://github.com/fortunexbt/world-watch">World Watch</a></b>
<br>Earthquakes, disaster alerts, storms and fires on one live map, every marker linked to its public record.
<br><a href="https://github.com/fortunexbt/world-watch">Code</a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://fortunexbt.github.io/solar-drift/"><img src="./assets/solar-drift.gif" alt="Solar Drift gameplay: looping around suns and crossing the wake to capture them" /></a>
<br><b><a href="https://github.com/fortunexbt/solar-drift">Solar Drift</a></b>
<br>Loop around a sun and cross your own wake to capture it. Canvas and procedural audio, nothing to install.
<br><a href="https://fortunexbt.github.io/solar-drift/">Play</a> · <a href="https://github.com/fortunexbt/solar-drift">Code</a>
</td>
<td width="50%" valign="top">
<a href="https://fortunexbt.github.io/loop-courier/"><img src="./assets/loop-courier.gif" alt="Loop Courier gameplay: drawing a delivery route through a city and dispatching the courier" /></a>
<br><b><a href="https://github.com/fortunexbt/loop-courier">Loop Courier</a></b>
<br>Draw one route through a seeded city and make every deadline. A new city every midnight.
<br><a href="https://fortunexbt.github.io/loop-courier/">Play</a> · <a href="https://github.com/fortunexbt/loop-courier">Code</a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://terminal-starfield.vercel.app/"><img src="./assets/terminal-starfield.gif" alt="Terminal Starfield: space combat drawn in terminal characters" /></a>
<br><b><a href="https://github.com/fortunexbt/terminal-starfield">Terminal Starfield</a></b>
<br>A space-combat roguelite for the terminal in pure Python. The browser version runs the same code on Pyodide.
<br><a href="https://terminal-starfield.vercel.app/">Play</a> · <a href="https://github.com/fortunexbt/terminal-starfield">Code</a>
</td>
<td width="50%" valign="top">
<a href="https://ckitty.vercel.app/"><img src="./assets/ckitty.gif" alt="ckitty: a cat drawn in terminal characters changing pose" /></a>
<br><b><a href="https://github.com/fortunexbt/ckitty">ckitty</a></b>
<br>A cat for your terminal, written in C. The browser version is the same code in 65 KB of WebAssembly.
<br><a href="https://ckitty.vercel.app/">Play</a> · <a href="https://github.com/fortunexbt/ckitty">Code</a>
</td>
</tr>
</table>

### Things I measured

- pandas, SQLite and DuckDB silently returned wrong totals on 12-17% of real Wikipedia-table questions. Tablebeam: 0.4%. [Eval](https://github.com/fortunexbt/tablebeam/tree/f141ee739f/eval)
- Claude Code kept calling write tools after the server said the budget was spent, in 5 of 5 runs. [Traces](https://github.com/fortunexbt/boundary-bench/tree/e937412/runs/2026-10-23-claude-code-haiku)
- Coding agents fell into loops of failing tool calls in 8.2% of 7,903 real sessions.
- A rule-based prompt-injection filter caught 0 of 320 attacks it was not written for.

Data, limits and the command that reproduces each one are on [fortunexbt.com](https://fortunexbt.com/#findings). Merged upstream: [google/adk-js#952](https://github.com/google/adk-js/pull/952).

[fortunexbt.com](https://fortunexbt.com) · [X](https://x.com/fortunexbt) · [Telegram](https://t.me/fortunexbt)
