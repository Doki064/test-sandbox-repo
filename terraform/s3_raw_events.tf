# Demo lakehouse bucket — intentional misconfigs for Prevue infra review

terraform {
  required_version = ">= 1.5"
}

resource "aws_s3_bucket" "raw_events" {
  bucket = "demo-lakehouse-raw-events"
}

# Intentionally public ACL (demo: iac-safety should flag)
resource "aws_s3_bucket_acl" "raw_events" {
  bucket = aws_s3_bucket.raw_events.id
  acl    = "public-read"
}

resource "aws_security_group" "etl" {
  name        = "demo-etl-sg"
  description = "ETL runners"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
