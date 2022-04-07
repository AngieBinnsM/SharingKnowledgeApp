provider "aws" {
    region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket = "sharing-knowledge-app.tfstate"
    key    = "sharing-knowldege-prod/terraform.tfstate"
    region = "us-east-1"
  }
}