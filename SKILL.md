---
name: you-got-this
description: >-
  Execute vague or detailed project goals autonomously while preserving the
  user's product intent. Inspect the real repository, infer safe missing
  details, establish an observable quality bar, implement, test, critique, and
  review the integrated result. Use for requests such as "$you-got-this make
  this prototype really good", finishing a project for public demonstration,
  substantial builds, polish passes, game work, or focused audits.
---

# You Got This

The user supplies intent. Determine the rest and act.

## Parse the invocation

- `$you-got-this <goal>`: execute the scoped goal autonomously.
- `$you-got-this gauntlet <goal>`: use the aggressive quality loop below.
- `$you-got-this audit` or `$you-got-this audit <area>`: inspect and report;
  do not implement major new functionality unless the request also clearly
  asks for fixes.
- Treat `gauntlet` and `audit` as mode words only when they are the first
  argument. Otherwise treat the whole message as the goal.

## Start with evidence

Before asking a question:

1. Find the actual project root and inspect its status.
2. Read applicable `AGENTS.md`, README files, project docs, tests, configs,
   assets, screenshots, and the code paths relevant to the goal.
3. Trace the user-visible or operational flow end to end. Run the cheapest
   useful checks and inspect real output where the task is visual or runtime-
   sensitive.
4. Infer non-critical missing details conservatively. Record important
   assumptions, decisions, blockers, and risks.

Ask only when the missing decision materially changes product scope, core user
intent, security or privacy, destructive or irreversible behavior, external
cost, or major compatibility expectations. Do not ask for implementation
details the repository can reveal or the agent can choose safely.

Preserve explicit instructions and existing product intent. Change
implementation freely when it improves the requested result, but escalate a
major direction change instead of silently replacing the idea.

## Set the quality bar

Choose the strongest practical, inspectable bar for the actual domain. Use a
provided reference; otherwise infer a credible shipped product, mature CLI,
reliable backend, ergonomic library, or equivalent target. Translate vague
words such as “good” or “production-ready” into observable checks: rendered
frames, behavior, latency, failure handling, accessibility, tests, recovery,
or other evidence that matters to this project.

Do not apply an irrelevant generic checklist. Inspect the dimensions that can
make this particular result weak: incomplete flows, empty/loading/error
states, keyboard and responsive behavior, performance, security, persistence,
onboarding, integration gaps, placeholders, documentation, or polish.

## Work

- Let the task determine the architecture and decomposition.
- Keep tightly coupled work under one coherent owner.
- Parallelize only genuinely independent work; integrate it before judging.
- For important quality-sensitive work, use a builder and a separate
  fresh-context critic when the host supports it. Have the critic inspect the
  actual result and the quality bar, not the builder’s summary.
- Implement the smallest complete change using existing patterns and
  dependencies. Do not add a framework, agent-management layer, state
  machine, database, scoreboard, or fixed team/iteration protocol.
- Run relevant tests and checks. For non-trivial logic leave one runnable
  regression check when the project has no better existing coverage.
- For visual or runtime work, inspect the integrated product, not only source,
  generated assets, a mockup, or a tool viewport.

For visual and game projects, choose the strongest available asset route:
reuse project assets first; use image generation for flat sprites, textures,
icons, UI art, or concepts; use real 3D tooling for geometry that must behave
as geometry; use code or shaders when they are the right fit. Always integrate
assets into the real product and judge the in-product result. Asset work never
replaces playable or usable product work. Note unavailable tools rather than
pretending their output was verified.

## Modes

### Default

Infer what is safe to infer, establish the quality bar, build, test, review,
and stop when no important actionable gap remains inside the intended scope,
further work has diminishing value, a capability blocks meaningful progress,
or a genuine product decision is required.

### Gauntlet

Use a stronger external reference and an aggressive but finite loop:

1. Build or improve the requested result against the reference.
2. Have a fresh critic inspect the real output and compare it with the bar.
3. Identify the largest remaining meaningful gap.
4. Fix that gap, then re-check the integrated result.
5. Use blind A/B comparison when it is genuinely useful and possible.

Repeat only while actionable, in-scope gaps remain. Do not make the loop
logically infinite, lower the reference, or replace product work with endless
asset generation or capture tooling.

### Audit

Do not turn an audit into a build by default. Inspect the requested area and
its neighboring flow, then report prioritized, actionable findings with exact
files or surfaces, evidence, impact, and the smallest useful next step. Make
only clearly requested fixes. Check integration, drift, risks, missing
requirements, and the highest-value improvement rather than producing a
ceremonial checklist.

## Game-aware pass

When the project is a game, automatically select the relevant dimensions from
the actual project: core loop, controls, movement, combat and game feel,
enemies or AI, level design, feedback, animation, VFX, audio, UI, visual
cohesion, asset quality, performance, onboarding, and playability. Compare
real in-game frames or interaction against the chosen reference. Do not let
art generation hide weak gameplay or let a capture setup make the game
unplayable.

## Lightweight progress

For a substantial task, maintain one concise project-local `.gauntlet.md` (or
an existing equally simple project-appropriate artifact) with only:

- Goal
- Quality bar
- Current focus
- Completed work
- Largest current gap
- Important assumptions, decisions, blockers, and likely next step

Create or update it only when it helps the user return later. Never build a
dashboard, round ledger, scoring service, or process around it.

## Completion gate

Before declaring completion:

1. Inspect the integrated real output.
2. Compare it with the chosen quality bar and check for product drift.
3. Run relevant tests and checks.
4. Use an independent final critic where the risk or quality sensitivity
   warrants it.
5. Perform a final domain-specific missing-things sweep.

Report what changed, what was checked, and what remains unverified. Never
claim browser, runtime, external integration, deployment, or human approval
without direct evidence.
