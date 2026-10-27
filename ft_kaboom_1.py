"""Exercise 4: the dark spellbook intentionally raises ImportError."""


def main() -> None:
    """Import the broken pair so the circular dependency is visible."""
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Forbidden", "bats and frogs"))


if __name__ == "__main__":
    main()
