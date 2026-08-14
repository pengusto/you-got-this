"""Small dependency-free checks for the published skill package."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
METADATA = ROOT / "agents" / "openai.yaml"
README = ROOT / "README.md"


def test_skill_front_matter() -> None:
    text = SKILL.read_text()
    assert text.startswith("---\n")
    assert "name: you-got-this" in text
    assert "description:" in text
    assert "# You Got This" in text
    assert len(text.splitlines()) >= 100


def test_codex_metadata() -> None:
    text = METADATA.read_text()
    assert "display_name: \"You Got This\"" in text
    assert "short_description:" in text
    assert "default_prompt:" in text


def test_docs_and_examples_are_linked() -> None:
    readme = README.read_text()
    examples = (ROOT / "examples.md").read_text()
    assert "examples.md" in readme
    assert "$you-got-this" in readme
    assert "$you-got-this gauntlet" in examples
    assert "$you-got-this audit" in examples


def main() -> None:
    for check in (
        test_skill_front_matter,
        test_codex_metadata,
        test_docs_and_examples_are_linked,
    ):
        check()
    print("ok: skill package validation passed")


if __name__ == "__main__":
    main()
