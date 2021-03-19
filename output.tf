output "iam_role_arn" {
  value = aws_iam_role.rds_lambda_role.arn
}

output "iam_role_id" {
  value = aws_iam_role.rds_lambda_role.id
}

output "instance_profile_arn" {
  value = aws_iam_instance_profile.rds_lambda_role.arn
}

output "instance_profile_id" {
  value = aws_iam_instance_profile.rds_lambda_role.id
}

output "cloudwatch_event_rule_arn" {
  value = aws_cloudwatch_event_rule.every_day.arn
}

output "cloudwatch_event_target_arn" {
  value = aws_cloudwatch_event_target.check_every_day.arn
}

output "lambda_function_arn" {
  value = aws_lambda_function.rds_lambda.arn
}
