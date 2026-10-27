"""Exercise 4: use the working light grimoire package interface."""

from alchemy.grimoire import light_spell_record


def main() -> None:
    """Record one light spell without triggering an import cycle."""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    recorded_spell = light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {recorded_spell}")


if __name__ == "__main__":
    main()
