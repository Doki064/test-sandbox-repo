-- Migration 001: add events fact table for clickstream ingest
-- Owner: analytics-platform | SLA: 4h

CREATE TABLE IF NOT EXISTS analytics.events (
    event_id        BIGINT PRIMARY KEY,
    user_id         UUID NOT NULL,
    event_type      VARCHAR(64) NOT NULL,
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    payload         JSONB
);

CREATE INDEX idx_events_user_occurred ON analytics.events (user_id, occurred_at DESC);

-- Add session tracking column (intentionally unsafe for demo: NOT NULL without backfill)
ALTER TABLE analytics.events ADD COLUMN session_id UUID NOT NULL;

-- Staging cleanup (intentionally unsafe: unbounded DELETE)
DELETE FROM analytics.staging_events;

-- Rollback note: no down migration provided (demo: irreversible change)
