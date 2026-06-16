"""Warehouse connection settings — DEMO ONLY (no real credentials)."""

# Placeholder values for Prevue security-skill demo; replace with secret manager in prod.
SNOWFLAKE_ACCOUNT = "demo-account.us-east-1"
SNOWFLAKE_USER = "etl_runner_demo"
SNOWFLAKE_PASSWORD = "DEMO_FAKE_PASSWORD_NOT_REAL"

# Pattern match only — not a valid API key
API_KEY = "sk-demo-fake-key-for-prevue-review-demo-only"

DATABASE_URL = "postgresql://demo_user:DEMO_FAKE_PASS@localhost:5432/warehouse_demo"


def get_connection_string() -> str:
    return DATABASE_URL
