"""Exercise 2: access only the names exported by the alchemy package."""

import alchemy


def main() -> None:
    """Show the public air function and the intentionally hidden earth one."""
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    hidden_earth = alchemy.create_earth()
    print(f"Testing the hidden create_earth: {hidden_earth}")


if __name__ == "__main__":
    main()
