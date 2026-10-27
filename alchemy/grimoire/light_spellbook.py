"""Light spells delegate ingredient checking to the light validator."""

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients accepted by light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a spell only when its ingredients pass validation."""
    result = validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
