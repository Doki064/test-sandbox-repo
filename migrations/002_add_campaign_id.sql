-- Migration 002: widen events payload for attribution (multi-label demo with Terraform)

ALTER TABLE analytics.events ADD COLUMN campaign_id VARCHAR(128);

CREATE INDEX idx_events_campaign ON analytics.events (campaign_id)
    WHERE campaign_id IS NOT NULL;

-- Intentionally missing CONCURRENTLY note for large-table demo
CREATE INDEX idx_events_occurred_brin ON analytics.events USING BRIN (occurred_at);
