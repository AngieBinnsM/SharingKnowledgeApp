provider "aws" {
    region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket = "mypgs-sandbox.tfstate"
    key    = "sharing-knowledge-prod/terraform.tfstate"
    region = "us-east-1"
  }
}
// add a comment
