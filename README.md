# Mario (fortunexbt)

I build infrastructure for running AI agents in production, and I measure whether agent safety controls hold up under real runs.

In October 2026 Google merged my security fix to its Agent Development Kit for JavaScript, which makes implicit Google API authentication require HTTPS ([google/adk-js#952](https://github.com/google/adk-js/pull/952)).

## MUTX

<a href="https://github.com/mutx-dev/mutx-dev"><img src="./assets/mutx.gif" width="800" alt="MUTX operator demo showing agent runs and their controls with illustrative data" /></a>

[MUTX](https://github.com/mutx-dev/mutx-dev) is a control plane for AI agents. Operators deploy agents with it, watch their runs, set budgets and approval rules, and stop any run. It has a FastAPI API with 249 route handlers, a Next.js dashboard, an Electron desktop app, a CLI and a Python SDK, covered by 2,460 Python and 876 TypeScript tests. Of its 737 commits on main, 575 are mine or my coding agents'. Counted at 782f2a33 on 22 October 2026. [Docs](https://docs.mutx.dev/)

## Findings

Measured results with the command that reproduces them, negatives included.

- Claude Code with claude-haiku-5-5 kept calling write tools after an MCP server said its budget was exhausted, in 5 of 5 runs (95% CI 57-100%). The server refused every extra call. [Traces and repro](https://github.com/fortunexbt/boundary-bench/tree/aacaeba/runs/2026-10-23-claude-code-haiku)
- AgentDojo's baseline prompt-injection template misspells "instructions", so filters keyed on that word miss it by accident. Reported upstream as [ethz-spylab/agentdojo#231](https://github.com/ethz-spylab/agentdojo/issues/231).

Methods and limits for each are on [fortunexbt.com](https://fortunexbt.com).

## Everything else

Experiments, tools and games live in [fortunexbt/lab](https://github.com/fortunexbt/lab).

I also build websites for local businesses through my studio, [Civico Due](https://civicodue.eu/).

[fortunexbt.com](https://fortunexbt.com) · [X](https://x.com/fortunexbt) · [Telegram](https://t.me/fortunexbt)
