resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.rds_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.every_day.arn
}

resource "aws_lambda_function" "rds_lambda" {
  filename      = "stop_rds.py.zip"
  function_name = "start_stop_rds"
  role          = aws_iam_role.rds_lambda_role.arn
  handler       = "stop_rds.lambda_handler"
  runtime       = "python3.7"
  memory_size   = 1024
  timeout       = 900
}

resource "aws_iam_role" "rds_lambda_role" {
  name               = "rds_stop_start_lambda_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_instance_profile" "rds_lambda_role" {
  name = "rds_stop_start_lambda_role"
  role = aws_iam_role.rds_lambda_role.name
}

resource "aws_iam_role_policy" "rds_policy" {
  name = "rds-admin-role-policy"
  role = aws_iam_role.rds_lambda_role.id

  policy = <<-EOF
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "rds:DescribeDBInstances",
                    "rds:StopDBInstance",
                    "rds:StartDBInstance"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "*"
            }
        ]
    }
  EOF
}
