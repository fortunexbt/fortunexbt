# Mario / Fortune

I work on infrastructure for running AI agents under human control, mainly at [MUTX](https://github.com/mutx-dev/mutx-dev). Most of the repositories below are small deterministic labs, each testing one part of that problem. I also build websites for local businesses through Civico Due, and write games on the side.

[Agents](#agent-infrastructure) · [Research tools](#research-tools) · [Websites](#client-websites) · [Games](#games) · [Background](#background)

<sub>The clips are recorded demos and can lag behind the code. Each repository has the current build.</sub>

## Agent infrastructure

### [MUTX](https://github.com/mutx-dev/mutx-dev)

A control plane for AI agents. It shows operators what each agent is doing and lets them set limits or stop a run.

<a href="https://github.com/mutx-dev/mutx-dev"><img src="./assets/motion/tools/mutx.gif" width="800" alt="MUTX operator demo showing agent runs and their controls with illustrative data" /></a>

<sub>Operator demo with illustrative data. [Documentation](https://docs.mutx.dev/) · [Upstream credits](https://github.com/mutx-dev/mutx-dev/blob/main/CREDITS.md)</sub>

## Research tools

<table>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/boundary-bench">BoundaryBench</a></h3><p>Crash tests for agent control planes. Each scenario checks that a stop, budget or approval blocks the forbidden action and lets permitted work continue. Synthetic data.</p><a href="https://github.com/fortunexbt/boundary-bench"><img src="./assets/motion/tools/boundary-bench.gif" width="100%" alt="BoundaryBench exploring synthetic agent-control test fixtures" /></a><p><a href="https://fortunexbt.github.io/boundary-bench/">Live demo ↗</a> · <a href="https://github.com/fortunexbt/boundary-bench">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/switchyard">Switchyard</a></h3><p>A local operator console with visible policy gates. The demo replays a captured incident so you can stop it and inspect the audit receipt it leaves.</p><a href="https://fortunexbt.github.io/switchyard/"><img src="./assets/motion/tools/switchyard.gif" width="100%" alt="Switchyard compact console showing a replay route, stop control and receipt ledger" /></a><p><a href="https://fortunexbt.github.io/switchyard/">Live demo ↗</a> · <a href="https://github.com/fortunexbt/switchyard">Code ↗</a></p></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/ambient-relay">Ambient Relay</a></h3><p>An offline Discord automation lab. Synthetic events pass through explicit policy checks, and each outcome leaves a receipt you can inspect.</p><a href="https://github.com/fortunexbt/ambient-relay"><img src="./assets/motion/tools/ambient-relay.gif" width="100%" alt="Ambient Relay processing synthetic events through policy checks" /></a><p><a href="https://github.com/fortunexbt/ambient-relay">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/queueglass">Queueglass</a></h3><p>A seeded discrete-event simulator for watching a queue back up under load and recover.</p><a href="https://github.com/fortunexbt/queueglass"><img src="./assets/motion/tools/queueglass.gif" width="100%" alt="Queueglass showing a simulated queue as its load changes" /></a><p><a href="https://github.com/fortunexbt/queueglass">Code ↗</a></p></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/tablebeam">Tablebeam</a></h3><p>Ask questions about a CSV or Google Sheet using a local model, and see the source rows behind each answer.</p><a href="https://github.com/fortunexbt/tablebeam"><img src="./assets/motion/tools/tablebeam.gif" width="100%" alt="Tablebeam interface answering a question from local data" /></a><p><a href="https://github.com/fortunexbt/tablebeam">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/barter">Barter Protocol Lab</a></h3><p>Replays synthetic commodity trades through a deterministic paper ledger.</p><a href="https://fortunexbt.github.io/barter/"><img src="https://raw.githubusercontent.com/fortunexbt/barter/main/assets/barter-protocol-lab.jpg" width="100%" alt="Barter Protocol Lab paper-ledger workbench replaying a simulated trade" /></a><p><a href="https://fortunexbt.github.io/barter/">Live demo ↗</a> · <a href="https://github.com/fortunexbt/barter">Code ↗</a></p></td>
  </tr>
</table>

## Client websites

<sub>Built for local businesses through [Civico Due](https://civicodue.eu/). The clips are recordings of the live sites.</sub>

<h3><a href="https://www.bottegapriori.com/">Bottega Dei Priori</a></h3>
<p>A restaurant site with bilingual menus and direct booking.</p>
<a href="https://www.bottegapriori.com/"><img src="./assets/motion/websites/bottega-priori.gif" width="600" alt="Scrolling through Bottega Dei Priori restaurant website and its food photography" /></a>
<p><a href="https://www.bottegapriori.com/">Visit website ↗</a></p>

<h3><a href="https://mudescoladeceramica.com/pt">MUD</a></h3>
<p>A site for a ceramics school, with a finder for its weekly classes.</p>
<a href="https://mudescoladeceramica.com/pt"><img src="./assets/motion/websites/mud-ceramica.gif" width="600" alt="MUD ceramic studio website and its class overview" /></a>
<p><a href="https://mudescoladeceramica.com/pt">Visit website ↗</a></p>

## Games

<table>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/solar-drift">Solar Drift</a></h3><p>An orbital arcade game. Draw a loop around a sun and cross your own wake to capture it. TypeScript and Canvas 2D.</p><a href="https://github.com/fortunexbt/solar-drift"><img src="./assets/motion/solar-drift.gif" width="100%" alt="Solar Drift ship closing an orbit and collecting a sun" /></a><p><a href="https://fortunexbt.github.io/solar-drift/">Play ↗</a> · <a href="https://github.com/fortunexbt/solar-drift">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/loop-courier">Loop Courier</a></h3><p>Draw one delivery route through a seeded city and make the deadlines with a limited number of route splices.</p><a href="https://github.com/fortunexbt/loop-courier"><img src="https://raw.githubusercontent.com/fortunexbt/loop-courier/main/assets/loop-courier-showcase.png" width="100%" alt="Loop Courier dispatch console showing a glowing delivery route, score, cargo and route controls" /></a><p><a href="https://fortunexbt.github.io/loop-courier/">Play ↗</a> · <a href="https://github.com/fortunexbt/loop-courier">Code ↗</a></p></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/terminal-starfield">Terminal Starfield</a></h3><p>A space combat roguelite that runs in the terminal with no dependencies.</p><a href="https://github.com/fortunexbt/terminal-starfield"><img src="./assets/motion/games/terminal-starfield.gif" width="100%" alt="Terminal Starfield flight deck and flagship worlds" /></a><p><a href="https://github.com/fortunexbt/terminal-starfield">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/ckitty">ckitty</a></h3><p>A terminal pet written in C11 and animated with ncurses.</p><a href="https://github.com/fortunexbt/ckitty"><img src="./assets/motion/games/ckitty.gif" width="100%" alt="A procedural terminal cat changing poses" /></a><p><a href="https://github.com/fortunexbt/ckitty">Code ↗</a></p></td>
  </tr>
</table>

## Background

I studied politics and international relations at Cardiff University and have worked in crypto research and governance. That's why most of my software deals with who can authorise an action and how someone checks it afterwards.

I use AI coding tools heavily. I decide what gets built and review and test what they produce, and I'm responsible for what ships.

Architecture write-ups and release evidence are in the [Field Manual](https://github.com/fortunexbt/docs). Open pull requests upstream include Discord hardening for [Hermes Agent](https://github.com/NousResearch/hermes-agent/pull/65575) and a plugin for [Open Design](https://github.com/nexu-io/open-design/pull/6427).

<details>
<summary>Repository index</summary>

<table>
  <tr><td><a href="https://github.com/fortunexbt/ambient-relay">ambient-relay</a></td><td>Offline Discord automation with explicit live gates.</td><td><a href="https://github.com/fortunexbt/ambient-relay">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/barter">barter</a></td><td>Replayable commodity-exchange protocol lab.</td><td><a href="https://github.com/fortunexbt/barter">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/boundary-bench">boundary-bench</a></td><td>Crash tests for agent control planes.</td><td><a href="https://github.com/fortunexbt/boundary-bench">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/ckitty">ckitty</a></td><td>Native C11 terminal companion.</td><td><a href="https://github.com/fortunexbt/ckitty">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/docs">docs</a></td><td>Architecture tours and reproducible release evidence.</td><td><a href="https://github.com/fortunexbt/docs">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/fieldwork-plugins">fieldwork-plugins</a></td><td>ChatGPT and Codex plugins for CSV analysis, release checks and 3D assets.</td><td><a href="https://github.com/fortunexbt/fieldwork-plugins">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/flock-baseline-runner">flock-baseline-runner</a></td><td>Paired A-B-B-A kernel experiments for the Flock BLAKE3 challenge.</td><td><a href="https://github.com/fortunexbt/flock-baseline-runner">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/loop-courier">loop-courier</a></td><td>Seeded route-drawing courier game.</td><td><a href="https://github.com/fortunexbt/loop-courier">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/minecraft-apple-silicon-framework">minecraft-apple-silicon-framework</a></td><td>Measured Minecraft shader setups for Apple Silicon.</td><td><a href="https://github.com/fortunexbt/minecraft-apple-silicon-framework">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/minecraft-frame-bench">minecraft-frame-bench</a></td><td>Minecraft frame-time measurements on macOS.</td><td><a href="https://github.com/fortunexbt/minecraft-frame-bench">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/queueglass">queueglass</a></td><td>Replayable queue pressure and recovery lab.</td><td><a href="https://github.com/fortunexbt/queueglass">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/solar-drift">solar-drift</a></td><td>Orbital arcade game for the browser.</td><td><a href="https://github.com/fortunexbt/solar-drift">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/switchyard">switchyard</a></td><td>Local operator console with visible policy gates.</td><td><a href="https://github.com/fortunexbt/switchyard">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/tablebeam">tablebeam</a></td><td>Local-model Q&amp;A over CSV files and Google Sheets.</td><td><a href="https://github.com/fortunexbt/tablebeam">↗</a></td></tr>
  <tr><td><a href="https://github.com/fortunexbt/terminal-starfield">terminal-starfield</a></td><td>Zero-dependency terminal combat roguelite.</td><td><a href="https://github.com/fortunexbt/terminal-starfield">↗</a></td></tr>
</table>
</details>

---

[Work and contact](https://fortunexbt.com) &nbsp; / &nbsp; [Telegram](https://t.me/fortunexbt) &nbsp; / &nbsp; [X](https://x.com/fortunexbt) &nbsp; / &nbsp; [Writing](https://fortunexbt.substack.com/)
