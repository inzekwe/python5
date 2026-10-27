"""Exercise 2: access the root-level elements module."""

import elements


def main() -> None:
    """Demonstrate importing a module by its root-level name."""
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
