# ETL runner IAM — demo misconfiguration

resource "aws_iam_role" "etl_runner" {
  name = "demo-etl-runner"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
    }]
  })
}

# Intentionally over-broad policy for demo
resource "aws_iam_role_policy" "etl_runner" {
  name = "demo-etl-runner-policy"
  role = aws_iam_role.etl_runner.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "*"
      Resource = "*"
    }]
  })
}

resource "aws_db_instance" "warehouse" {
  identifier        = "demo-warehouse"
  engine            = "postgres"
  instance_class    = "db.t3.micro"
  allocated_storage = 20
  username          = "admin"
  password          = "hardcoded-demo-password"
  publicly_accessible = true
  skip_final_snapshot = true
}
