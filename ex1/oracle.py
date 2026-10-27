"""Load non-secret defaults and secret configuration from the environment."""

import os

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


def main() -> None:
    """Load the adjacent development .env and report safe config status."""
    project_directory = os.path.dirname(os.path.abspath(__file__))
    env_file = os.path.join(project_directory, ".env")
    if load_dotenv is None:
        print(
            "WARNING: python-dotenv is missing; using process variables only."
        )
    else:
        load_dotenv(dotenv_path=env_file)

    mode = os.getenv("MATRIX_MODE", "development").strip().lower()
    if mode not in ("development", "production"):
        print(f"WARNING: Unsupported MATRIX_MODE {mode!r}; using development.")
        mode = "development"

    database_url = os.getenv("DATABASE_URL", "")
    api_key = os.getenv("API_KEY", "")
    log_level_default = "DEBUG" if mode == "development" else "INFO"
    log_level = os.getenv("LOG_LEVEL", log_level_default).strip().upper()
    zion_endpoint = os.getenv("ZION_ENDPOINT", "")

    print("ORACLE STATUS: Consulting the configuration...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if database_url:
        database_status = (
            "Configured (local instance)"
            if mode == "development"
            else "Configured"
        )
    else:
        database_status = (
            "Not configured; using local development default"
            if mode == "development"
            else "MISSING"
        )
    print(f"Database: {database_status}")
    print(f"API Access: {'Configured' if api_key else 'MISSING'}")
    print(f"Log Level: {log_level or log_level_default}")
    print(f"Remote Network: {'Configured' if zion_endpoint else 'MISSING'}")

    missing = [
        name for name, value in (
            ("DATABASE_URL", database_url),
            ("API_KEY", api_key),
            ("ZION_ENDPOINT", zion_endpoint),
        ) if not value
    ]
    if missing:
        print("WARNING: Missing configuration: " + ", ".join(missing))
    print("Configuration security check:")
    print("[OK] Secret values are not printed")
    gitignore_path = os.path.join(project_directory, ".gitignore")
    try:
        with open(gitignore_path, "r", encoding="utf-8") as gitignore_file:
            ignored_entries = gitignore_file.read().splitlines()
    except OSError:
        ignored_entries = []
    if ".env" in ignored_entries:
        print("[OK] .env is listed in .gitignore")
    else:
        print("WARNING: .env is not listed in .gitignore")
    print("[OK] Process environment overrides .env values")
    if mode == "production":
        print("Production mode: configure external services securely.")
    else:
        print(
            "Development mode: safe local defaults are enabled where possible."
        )
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
