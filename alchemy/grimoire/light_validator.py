"""Validate light ingredients while avoiding an import-time cycle."""


def validate_ingredients(ingredients: str) -> str:
    """Check case-insensitively whether any permitted ingredient is present.

    The spellbook imports this module at load time. Importing the spellbook
    inside this function delays the reverse dependency until both modules have
    finished initializing, breaking the circular import safely.
    """
    from .light_spellbook import light_spell_allowed_ingredients

    normalized = ingredients.lower()
    is_valid = any(
        allowed in normalized for allowed in light_spell_allowed_ingredients()
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
