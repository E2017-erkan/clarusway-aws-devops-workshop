provider "aws" {
  region = "us-east-1"
}
locals {
  my-instance-name = "oliver-locals"
  my-instance-type = "t2.micro"
}
resource "aws_instance" "tf-example-ec2" {
  ami           = var.ec2-ami
  instance_type = local.my-instance-type
  key_name      = "northvirginia"
  tags = {
    Name = local.my-instance-name
  }
}
resource "aws_s3_bucket" "tf-example-s3" {
  bucket = var.s3-bucket-name
  acl    = "private"
  count = var.num_of_buckets
}
output "tf-example-public-ip" {
  value = aws_instance.tf-example-ec2.public_ip
}
output "tf-xample-s3-meta" {
  value = aws_s3_bucket.tf-example-s3
}
output "tf-example-private-ip" {
  value = aws_instance.tf-example-ec2.private_ip
}