"""Exercise 3: reach a recipe in the nested transmutation subpackage."""

from alchemy.transmutation.recipes import lead_to_gold


def main() -> None:
    """Run the nested recipe through a direct module import."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {lead_to_gold()}")


if __name__ == "__main__":
    main()
