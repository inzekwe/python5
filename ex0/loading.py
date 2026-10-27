"""Check the declared data-science dependencies without failing when absent."""

import importlib


REAGENTS = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
}


def main() -> None:
    """Report installed reagents and show pip/Poetry install commands."""
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")
    missing = []

    for module_name, description in REAGENTS.items():
        try:
            module = importlib.import_module(module_name)
        except ImportError:
            missing.append(module_name)
            print(f"[MISSING] {module_name}")
            continue

        version = getattr(module, "__version__", "version unavailable")
        print(f"[OK] {module_name} ({version}) - {description}")

    print("pip vs Poetry:")
    print(
        "requirements.txt declares dependencies; pip resolves them on install."
    )
    print(
        "pyproject.toml declares the same constraints, and Poetry pins the"
    )
    print("versions in poetry.lock so every install is identical.")

    if missing:
        print("Some reagents are missing. Install them with:")
        print("pip install -r ex0/requirements.txt")
        print("poetry install (from the ex0 directory)")
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
