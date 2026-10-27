"""Inspect Python's current environment and explain how to isolate it."""

import os
import site
import sys


def _global_package_path() -> str:
    """Build the usual global site-packages path without extra imports."""
    version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    if os.name == "nt":
        return os.path.join(sys.base_prefix, "Lib", "site-packages")
    return os.path.join(sys.base_prefix, "lib", version, "site-packages")


def main() -> None:
    """Report whether this interpreter belongs to a virtual environment."""
    in_venv = sys.prefix != sys.base_prefix or hasattr(sys, "real_prefix")
    print(f"Current Python: {sys.executable}")

    if in_venv:
        environment_name = os.path.basename(os.path.normpath(sys.prefix))
        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"Virtual Environment: {environment_name}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        package_paths = site.getsitepackages()
        if package_paths:
            print("Reagent installation path:")
            print(package_paths[0])
        else:
            print("Reagent installation path: unavailable")
        print(f"Global package path: {_global_package_path()}")
        return

    print("LABORATORY STATUS: You are working in the open")
    print("Virtual Environment: None detected")
    print("Global package path:", _global_package_path())
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print(r"lab_env\Scripts\activate # On Windows")
    print("Then run this program again.")


if __name__ == "__main__":
    main()
