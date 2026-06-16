"""Nightly rollup of events into daily aggregates."""

from __future__ import annotations

from datetime import date


def run_rollup(run_date: date) -> int:
    """Missing owner/sla_hours docstring — violates custom pipeline-standards skill."""
    query = f"""
        INSERT INTO analytics.daily_event_counts (day, event_type, cnt)
        SELECT DATE(occurred_at), event_type, COUNT(*)
        FROM analytics.events
        WHERE occurred_at >= '{run_date.isoformat()}'
        GROUP BY 1, 2
    """
    # Intentionally no row-count logging (pipeline-standards skill)
    return execute_sql(query)


def execute_sql(sql: str) -> int:
    return 0
