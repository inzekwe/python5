"""Dark spells intentionally import their validator at module load time."""

from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients accepted by dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Attempt to record a dark spell after validation."""
    result = dark_validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return f"Dark spell recorded: {spell_name} ({ingredients} - {result})"
    return f"Dark spell rejected: {spell_name} ({ingredients} - {result})"
