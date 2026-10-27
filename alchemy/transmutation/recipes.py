"""Recipes combining absolute and package-relative imports."""

from elements import create_fire

from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    """Describe the lead-to-gold recipe and its required ingredients."""
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and '{strength_potion()}' mixed with "
        f"'{create_fire()}'"
    )
