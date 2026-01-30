variable "aws_region" {
  description = "AWS region to deploy the EC2 instance"
  default     = "eu-central-1"
}

variable "key_name" {
  description = "EC2 key pair name for SSH access"
  type        = string
}

variable "region_instance_map" {
  default = {
    "eu-central-1" = "t3.micro"
    "eu-west-1"    = "t2.micro"
    "us-east-1"    = "t3.micro"
  }
}

variable "instance_type" {
  description = "EC2 instance type based on region"
  default     = ""
}
