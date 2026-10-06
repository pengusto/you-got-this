# You Got This

An autonomous project-execution skill for Codex and compatible agent harnesses.

You provide the intent. The skill finds the real project context, chooses a practical quality bar, implements the smallest complete change, verifies the result, and stops when the work is genuinely handled.

## Install

### Codex

Use an unused destination directory:

```sh
mkdir -p ~/.codex/skills
git clone https://github.com/pengusto/you-got-this.git ~/.codex/skills/you-got-this
```

Start a new agent session if the skill is not yet listed, then invoke it with:

```text
$you-got-this <goal>
```

### Update

```sh
git -C ~/.codex/skills/you-got-this pull --ff-only
```

## Modes

| Invocation | Use it for |
| --- | --- |
| `$you-got-this <goal>` | Normal autonomous execution, verification, and handoff |
| `$you-got-this gauntlet <goal>` | A finite build → critique → fix → re-check loop |
| `$you-got-this audit [area]` | Evidence-backed findings without a major implementation |

The mode word only applies when it is the first argument. A goal containing “audit” or “gauntlet” is still treated as a normal goal unless it starts with that mode.

See [examples.md](examples.md) for prompts and expected mode selection.

## What it does

- finds the actual repository and reads its governing instructions;
- traces the affected user-visible or operational flow;
- infers safe details instead of blocking on low-value questions;
- sets a concrete quality bar for the domain;
- implements the smallest complete change using existing patterns;
- runs relevant checks and distinguishes local evidence from unverified runtime or deployment gates;
- preserves product intent and surfaces decisions that genuinely need the user.

It does not create a framework, scoreboard, state machine, or process layer around the work. The repository and its existing tools remain the source of truth.

## Repository layout

```text
.
├── SKILL.md                 # Canonical skill instructions
├── agents/openai.yaml       # Codex display metadata
├── examples.md              # Prompt examples and expected mode selection
├── tests/test_skill.py      # Dependency-free structural validation
├── .github/workflows/       # Validation on every push and pull request
├── CHANGELOG.md
└── LICENSE
```

## Validate locally

```sh
python3 tests/test_skill.py
```

No package installation is required.

## Contributing

Keep changes focused on better decisions, safer execution, clearer evidence, and less unnecessary ceremony. If a rule cannot be checked or does not improve outcomes, it probably does not belong in the skill.

Run the validator before opening a pull request and include the behavior or failure mode the change improves.

## License

MIT. See [LICENSE](LICENSE).
