"""Dark validation naively imports the spellbook and creates a cycle."""

from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    """Check dark ingredients; importing this module intentionally explodes."""
    normalized = ingredients.lower()
    is_valid = any(
        allowed in normalized for allowed in dark_spell_allowed_ingredients()
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
