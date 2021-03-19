resource "aws_cloudwatch_event_rule" "every_day" {
  name                  = "stop-rds"
  description           = "Fires every day to stop rds"
  schedule_expression   = "rate(1 day)"
}

resource "aws_cloudwatch_event_target" "check_every_day" {
  rule        = aws_cloudwatch_event_rule.every_day.name
  target_id   = "lambda"
  arn         = aws_lambda_function.rds_lambda.arn
  input       = {"action": "stop","dbInstance": "rds-name"}
}
