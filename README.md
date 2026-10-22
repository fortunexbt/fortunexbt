# Mario / Fortune

I build software for running AI agents in production without losing control of them. My main project is [MUTX](https://github.com/mutx-dev/mutx-dev), a control plane I've built largely on my own since March 2026. The smaller repositories below each test one piece of that problem in isolation.

Python and TypeScript day to day, C when it needs to be small. FastAPI, Next.js, Electron, Postgres, Terraform and Helm.

[MUTX](#mutx) · [Research tools](#research-tools) · [Benchmarks](#benchmarks) · [Websites](#websites) · [Games](#games) · [Background](#background)

## MUTX

<a href="https://github.com/mutx-dev/mutx-dev"><img src="./assets/motion/tools/mutx.gif" width="800" alt="MUTX operator demo showing agent runs and their controls with illustrative data" /></a>

<sub>Operator demo with illustrative data. [Documentation](https://docs.mutx.dev/) · [Upstream credits](https://github.com/mutx-dev/mutx-dev/blob/main/CREDITS.md)</sub>

An operator deploys agents through MUTX, watches their runs, sets budgets and approval rules, and can stop any run. I wrote 913 of its commits, and the other contributors are bots. The current release is v1.4.0.

| Part | What it is |
| --- | --- |
| Control plane API | FastAPI, SQLAlchemy and asyncpg. 249 route handlers in 37 modules, covering auth, deployments, runs, budgets, approvals, webhooks and RAG |
| Operator dashboard | Next.js and React |
| Desktop app | Electron, with macOS builds for Apple silicon and Intel shipped alongside SHA-256 checksums |
| CLI and TUI | Click and Textual, installed through a [Homebrew tap](https://github.com/mutx-dev/homebrew-tap) |
| Python SDK | Client for the full `/v1` API |
| Access control | Role-based access with OIDC sign-in through Okta, Auth0, Azure AD or Keycloak |
| Infrastructure | Docker Compose locally, Terraform, Ansible and Helm in the cloud, with infrastructure drift checked in CI |
| Tests | About 2,460 Python tests and 876 TypeScript tests, plus Playwright end-to-end runs |
| Release | Five tagged releases. CI promotes builds to production on Railway |

## Research tools

Smaller labs, most of them seeded and deterministic so a run can be replayed exactly and the result checked.

<table>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/boundary-bench">BoundaryBench</a></h3><p>Crash tests for agent control planes. Each scenario checks that a stop, budget or approval blocks the forbidden action and lets permitted work continue. Every failure links to the trace events that caused it.</p><a href="https://github.com/fortunexbt/boundary-bench"><img src="./assets/motion/tools/boundary-bench.gif" width="100%" alt="BoundaryBench results: opening a failed budget scenario, its cited trace event, then the guarded candidate passing" /></a><p><sub>TypeScript. CI with CodeQL scanning.</sub><br><a href="https://fortunexbt.github.io/boundary-bench/">Live demo ↗</a> · <a href="https://github.com/fortunexbt/boundary-bench">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/switchyard">Switchyard</a></h3><p>A local operator console with visible policy gates. The demo replays a captured incident so you can stop it and inspect the audit receipt it leaves.</p><a href="https://fortunexbt.github.io/switchyard/"><img src="./assets/motion/tools/switchyard.gif" width="100%" alt="Switchyard compact console showing a replay route, stop control and receipt ledger" /></a><p><sub>TypeScript front end, Python backend.</sub><br><a href="https://fortunexbt.github.io/switchyard/">Live demo ↗</a> · <a href="https://github.com/fortunexbt/switchyard">Code ↗</a></p></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/tablebeam">Tablebeam</a></h3><p>Ask questions about a CSV or Google Sheet with a local model, and see the source rows behind each answer. Works with LM Studio, Ollama or any OpenAI-compatible server.</p><a href="https://github.com/fortunexbt/tablebeam"><img src="./assets/motion/tools/tablebeam.gif" width="100%" alt="Tablebeam interface answering a question from local data" /></a><p><sub>Python. v2.0.0.</sub><br><a href="https://github.com/fortunexbt/tablebeam">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/barter">Barter Protocol Lab</a></h3><p>A commodity barter state machine replayed from a fixed event journal. Each step recomputes the derived state and the journal hash from the events.</p><a href="https://fortunexbt.github.io/barter/"><img src="./assets/motion/tools/barter.gif" width="100%" alt="Barter Protocol Lab playing a copper for coffee exchange from Listed through to Settled" /></a><p><sub>TypeScript, full stack.</sub><br><a href="https://fortunexbt.github.io/barter/">Live demo ↗</a> · <a href="https://github.com/fortunexbt/barter">Code ↗</a></p></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/ambient-relay">Ambient Relay</a></h3><p>An offline Discord automation lab. Synthetic events pass through explicit policy checks, and each outcome leaves a receipt you can inspect.</p><a href="https://github.com/fortunexbt/ambient-relay"><img src="./assets/motion/tools/ambient-relay.gif" width="100%" alt="Ambient Relay processing synthetic events through policy checks" /></a><p><sub>JavaScript.</sub><br><a href="https://github.com/fortunexbt/ambient-relay">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/queueglass">Queueglass</a></h3><p>A seeded discrete-event simulator for watching a queue back up under load and recover.</p><a href="https://github.com/fortunexbt/queueglass"><img src="./assets/motion/tools/queueglass.gif" width="100%" alt="Queueglass showing a simulated queue as its load changes" /></a><p><sub>TypeScript.</sub><br><a href="https://github.com/fortunexbt/queueglass">Code ↗</a></p></td>
  </tr>
</table>

## Benchmarks

- [flock-baseline-runner](https://github.com/fortunexbt/flock-baseline-runner) runs the unchanged Flock BLAKE3 challenge on GitHub-hosted runners, then tests single small kernel changes in A-B-B-A order on the same machine so the comparison holds.
- [minecraft-frame-bench](https://github.com/fortunexbt/minecraft-frame-bench) and [minecraft-apple-silicon-framework](https://github.com/fortunexbt/minecraft-apple-silicon-framework) measure real frame times for Minecraft Java shader setups on Apple silicon, over timed routes.

## Websites

Designed and built through my studio, [Civico Due](https://civicodue.eu/). Bottega Dei Priori and MUD are shared work with Walberth Soares. Each clip is a 50fps capture of the live site.

<table>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://civicodue.eu/">Civico Due</a></h3><p>The studio's own site, built around a scroll-driven phone sequence.</p><a href="https://civicodue.eu/"><img src="./assets/motion/websites/civico-due.gif" width="100%" alt="Civico Due homepage scrolling through its phone sequence and services" /></a></td>
    <td width="50%" valign="top"><h3><a href="https://www.bottegapriori.com/">Bottega Dei Priori</a></h3><p>A trattoria in Perugia, with bilingual menus and booking over WhatsApp.</p><a href="https://www.bottegapriori.com/"><img src="./assets/motion/websites/bottega-priori.gif" width="100%" alt="Bottega Dei Priori homepage scrolling from the food hero into the dining room photos" /></a></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://mudescoladeceramica.com/pt">MUD</a></h3><p>A ceramics school in Leblon, Rio de Janeiro, with a finder for its weekly classes.</p><a href="https://mudescoladeceramica.com/pt"><img src="./assets/motion/websites/mud-ceramica.gif" width="100%" alt="MUD homepage scrolling from the studio hero into the class overview" /></a></td>
    <td width="50%" valign="top"><h3><a href="https://antico-frantoio-nunzi.vercel.app/">Antico Frantoio Nunzi</a></h3><p>A redesign proposal for an olive mill in Bevagna that has pressed oil since 1860.</p><a href="https://antico-frantoio-nunzi.vercel.app/"><img src="./assets/motion/websites/antico-frantoio-nunzi.gif" width="100%" alt="Antico Frantoio Nunzi redesign scrolling from the mill at night into its history" /></a></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://www.victoriainaudi.com/">Victoria Inaudi</a></h3><p>A poet's site in Spanish, Italian, Portuguese and English, with an editing panel for the author.</p><a href="https://www.victoriainaudi.com/"><img src="./assets/motion/websites/victoria-inaudi.gif" width="100%" alt="Victoria Inaudi homepage scrolling from the portrait into the poems" /></a></td>
    <td width="50%" valign="top"><h3><a href="https://elisapanzavolta.com/">Elisa Panzavolta</a></h3><p>A psychologist's practice in Perugia, with events and booking for a first consultation.</p><a href="https://elisapanzavolta.com/"><img src="./assets/motion/websites/elisa-panzavolta.gif" width="100%" alt="Elisa Panzavolta homepage scrolling from the hero into upcoming events" /></a></td>
  </tr>
</table>

## Games

<table>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/solar-drift">Solar Drift</a></h3><p>An orbital arcade game. Draw a loop around a sun and cross your own wake to capture it. TypeScript, Canvas 2D and procedural WebAudio.</p><a href="https://github.com/fortunexbt/solar-drift"><img src="./assets/motion/solar-drift.gif" width="100%" alt="Solar Drift ship closing an orbit and collecting a sun" /></a><p><a href="https://fortunexbt.github.io/solar-drift/">Play ↗</a> · <a href="https://github.com/fortunexbt/solar-drift">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/loop-courier">Loop Courier</a></h3><p>Draw one delivery route through a seeded city and make the deadlines with a limited number of route splices.</p><a href="https://github.com/fortunexbt/loop-courier"><img src="https://raw.githubusercontent.com/fortunexbt/loop-courier/main/assets/loop-courier-showcase.png" width="100%" alt="Loop Courier dispatch console showing a glowing delivery route, score, cargo and route controls" /></a><p><a href="https://fortunexbt.github.io/loop-courier/">Play ↗</a> · <a href="https://github.com/fortunexbt/loop-courier">Code ↗</a></p></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/terminal-starfield">Terminal Starfield</a></h3><p>A space combat roguelite that runs in the terminal, written in Python with no dependencies.</p><a href="https://github.com/fortunexbt/terminal-starfield"><img src="./assets/motion/games/terminal-starfield.gif" width="100%" alt="Terminal Starfield flight deck and flagship worlds" /></a><p><a href="https://github.com/fortunexbt/terminal-starfield">Code ↗</a></p></td>
    <td width="50%" valign="top"><h3><a href="https://github.com/fortunexbt/ckitty">ckitty</a></h3><p>A terminal pet in C11 and ncurses, released as Linux and macOS binaries with checksums.</p><a href="https://github.com/fortunexbt/ckitty"><img src="./assets/motion/games/ckitty.gif" width="100%" alt="A procedural terminal cat changing poses" /></a><p><a href="https://github.com/fortunexbt/ckitty">Code ↗</a></p></td>
  </tr>
</table>

## Background

I studied politics and international relations at Cardiff University and have worked in crypto research and governance. That's why most of my software deals with who can authorise an action and how someone checks it afterwards.

I use AI coding tools heavily. I decide what gets built and review and test what they produce, and I'm responsible for what ships. Every repository of mine listed here runs CI on GitHub Actions.

Architecture write-ups and release evidence are in the [Field Manual](https://github.com/fortunexbt/docs). Open pull requests upstream include Discord hardening for [Hermes Agent](https://github.com/NousResearch/hermes-agent/pull/65575) and a plugin for [Open Design](https://github.com/nexu-io/open-design/pull/6427).

<details>
<summary>Repository index</summary>

<table>
  <tr><td><a href="https://github.com/fortunexbt/ambient-relay">ambient-relay</a></td><td>Offline Discord automation with explicit live gates.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/barter">barter</a></td><td>Replayable commodity-exchange protocol lab.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/boundary-bench">boundary-bench</a></td><td>Crash tests for agent control planes.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/ckitty">ckitty</a></td><td>Native C11 terminal companion.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/docs">docs</a></td><td>Architecture tours and reproducible release evidence.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/fieldwork-plugins">fieldwork-plugins</a></td><td>ChatGPT and Codex plugins for CSV analysis, release checks and 3D assets.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/flock-baseline-runner">flock-baseline-runner</a></td><td>Paired A-B-B-A kernel experiments for the Flock BLAKE3 challenge.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/loop-courier">loop-courier</a></td><td>Seeded route-drawing courier game.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/minecraft-apple-silicon-framework">minecraft-apple-silicon-framework</a></td><td>Measured Minecraft shader setups for Apple silicon.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/minecraft-frame-bench">minecraft-frame-bench</a></td><td>Minecraft frame-time measurements on macOS.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/queueglass">queueglass</a></td><td>Replayable queue pressure and recovery lab.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/solar-drift">solar-drift</a></td><td>Orbital arcade game for the browser.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/switchyard">switchyard</a></td><td>Local operator console with visible policy gates.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/tablebeam">tablebeam</a></td><td>Local-model Q&amp;A over CSV files and Google Sheets.</td></tr>
  <tr><td><a href="https://github.com/fortunexbt/terminal-starfield">terminal-starfield</a></td><td>Zero-dependency terminal combat roguelite.</td></tr>
</table>
</details>

---

[Work and contact](https://fortunexbt.com) &nbsp; / &nbsp; [Telegram](https://t.me/fortunexbt) &nbsp; / &nbsp; [X](https://x.com/fortunexbt) &nbsp; / &nbsp; [Writing](https://fortunexbt.substack.com/)
