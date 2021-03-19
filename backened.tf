terraform {
 backend "s3" {
   bucket                   = "aboi"
   key                      = "terraform/lambda/terraform_lambda.tfstate"
   region                   = "us-east-1"
   profile                  = "abasa"
   shared_credentials_file  = "~/.aws/credentials"
 }
}