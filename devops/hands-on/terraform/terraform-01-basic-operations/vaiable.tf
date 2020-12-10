# variable "ec2-name" {
#   default     = "oliver-new-ec2"
#   description = "name for ec2"
# }
# variable "ec2-type" {
#   default     = "t2.micro"
#   description = "type for ec2"
# }
variable "ec2-ami" {
  default     = "ami-04d29b6f966df1537"
  description = "ami for ec2"
}
variable "s3-bucket-name" {
  default     = "oliver-new-s3-bucket-2"
  description = "name for new s3 bucket"
}
variable "num_of_buckets" {
  default = 1
}