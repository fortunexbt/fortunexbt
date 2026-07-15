# Fortune / Mario

I build systems that have to survive contact with reality.

Right now that means **[MUTX](https://mutx.dev)**: infrastructure for seeing, controlling, and proving what AI agents do in production. Around it, I work on local-first AI, onchain coordination, regulated workflows, market infrastructure, and small terminal programs that are useful for no reason other than joy.

[MUTX](https://mutx.dev) · [GitHub](https://github.com/fortunexbt) · [Docs](https://docs.mutx.dev) · [X](https://x.com/FortuneXBT) · [Telegram](https://t.me/fortunexbt) · [Email](mailto:mario@mutx.dev)

---

## The main work

### [MUTX](https://github.com/mutx-dev/mutx-dev)

**The control plane around the agent.** MUTX keeps identity, runs, permissions, budgets, approvals, observability, and audit history in one operating surface.

It ships as more than a dashboard:

- a FastAPI control plane with explicit `/v1/*` contracts
- an authenticated web operator and guided browser demo
- a signed and notarized macOS app
- a Python CLI, Textual TUI, and first-party SDK
- local and hosted setup paths
- Docker, Terraform, Ansible, Helm, and monitoring assets
- policy enforcement, credential brokering, session budgets, and review gates

<a href="https://mutx.dev">
  <img src="https://raw.githubusercontent.com/mutx-dev/mutx-dev/main/public/demo.gif" alt="MUTX operator dashboard showing an agent run" width="100%" />
</a>

**[Try the product](https://mutx.dev)** · **[Read the code](https://github.com/mutx-dev/mutx-dev)** · **[Open the docs](https://docs.mutx.dev)** · **[Download for macOS](https://mutx.dev/download/macos)**

---

## Open source

| Project | What shipped |
|---|---|
| **[Tablebeam](https://github.com/fortunexbt/tablebeam)** | Private-by-default Q&A for CSV and Google Sheets. Runs against LM Studio, Ollama, or any local OpenAI-compatible model; every answer points back to the source rows. |
| **[ckitty](https://github.com/fortunexbt/ckitty)** | A tiny native terminal cat in C11 and ncurses. Procedural poses, deterministic rendering, resize-safe animation, tests, sanitizers, and no runtime baggage. |
| **[SecurePath](https://github.com/fortunexbt/securepath)** | A production-minded Discord research agent for crypto and DeFi: chart vision, contextual conversations, caching, rate control, and operational telemetry. |
| **[BarterTrade](https://github.com/fortunexbt/barter)** | A full-stack commodity barter platform with real-time offers, identity workflows, AI-assisted matching, and privacy-preserving verification experiments. |
| **[Terminal Starfield](https://github.com/fortunexbt/terminal-starfield)** | A dependency-free, interactive 3D starfield for the terminal with warp, trails, density controls, and color modes. |
| **[MUTX Homebrew Tap](https://github.com/mutx-dev/homebrew-tap)** | The maintained install path for the MUTX CLI on macOS. |

<details>
<summary><strong>A very small demo</strong></summary>
<br>

<a href="https://github.com/fortunexbt/ckitty">
  <img src="https://raw.githubusercontent.com/fortunexbt/ckitty/main/assets/ckitty-demo.gif" alt="ckitty animated terminal demo" width="100%" />
</a>

</details>

---

## Closed-source work

The repositories are private; the problems are real. This is the part I can describe publicly.

| System | What it does |
|---|---|
| **OpenRNA Foundry** | A local-only RNA construct review and design-triage workbench. Deterministic sequence scoring, synonymous codon optimization, IVT specification assembly, evidence capture, specialist review agents, and research-PDF workflows—with no telemetry or cloud dependency. |
| **Cipher** | An autonomous, oracle-aware agent built around programmable onchain behavior, market context, and economic constraints. |
| **TCE12 / SecurePath** | Cross-border governance and settlement infrastructure: compliance attestations, milestone escrow, royalties, offtake agreements, and proof-of-settlement audit packets. |
| **MUTX operations** | The private delivery layer behind the public product: runtime operations, deployment infrastructure, authentication, webhooks, API keys, and production control surfaces. |
| **Market intelligence systems** | Crypto research agents, seed-stage discovery, portfolio and treasury monitoring, vehicle-market data pipelines, and decision-support workflows. |
| **AI operator systems** | Closed-loop research, qualification, outreach, follow-up, QA, and reporting systems built around measurable commercial outcomes. |

### Client products and independent experiments

- **SecurePath Academy** — education and research product
- **[MUD Escola de Cerâmica](https://mudescoladeceramica.com)** — multilingual product and commerce surface
- **[Cavapendolandia](https://cavapendo.land/)** — minimalist art platform
- bilingual hospitality, wellness, and commerce builds
- ambient Discord agents and community intelligence tools
- **Loop Courier** and **Neon Rogue Snake** — small game experiments

---

## Before the control plane

I came to software through crypto research and institution-facing infrastructure: staking economics, validator governance, custody architecture, MEV, rollups, token design, treasury strategy, and derivatives research.

That work included building **SecurePath**, institutional staking research at **Colossus Digital**, quantitative crypto research at **Optimum Complexity**, co-founding **AlphaBlock Network**, and contributing tokenomics and governance work to **Cerebrum DAO**.

It still shapes how I build: explicit incentives, bounded authority, observable state, and systems that can explain what happened after the demo ends.

---

## Working set

**Languages** — Python, TypeScript, Solidity, C, SQL, Bash<br>
**Product** — FastAPI, React, Next.js, PostgreSQL, Redis, Docker<br>
**Infrastructure** — Terraform, Ansible, Helm, CI/CD, observability<br>
**Human languages** — English, Italian, Spanish, Portuguese; basic German

If you are building agent infrastructure, local-first AI, or economically serious onchain systems, **[get in touch](mailto:mario@mutx.dev)**.
