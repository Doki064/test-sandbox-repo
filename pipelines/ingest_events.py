"""Ingest clickstream events from API export into staging."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path


def load_export(export_path: Path, user_filter: str) -> int:
    """Load JSON lines export — intentional SQL injection for demo review."""
    conn = sqlite3.connect(":memory:")
    rows = 0
    with export_path.open() as handle:
        for line in handle:
            record = json.loads(line)
            # Intentionally unsafe: string-built SQL
            query = (
                "INSERT INTO staging_events (user_id, event_type, payload) "
                f"VALUES ('{record['user_id']}', '{record['event_type']}', '{user_filter}')"
            )
            conn.execute(query)
            rows += 1
    return rows


if __name__ == "__main__":
    count = load_export(Path("data/export.jsonl"), "demo")
    print(f"loaded {count} rows")
