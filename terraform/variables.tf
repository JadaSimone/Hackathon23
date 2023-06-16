variable "access_key" {
        description = "Access key to AWS console"
}
variable "secret_key" {
        description = "Secret key to AWS console"
}

variable "request_id" {
  default = "random234323"
}

variable "instance_name" {
        description = "Name of the instance to be created"
        default = "awsbuilder-demo"
}

variable "instance_type" {
        default = "t2.micro"
}

variable "subnet_id" {
        description = "The VPC subnet the instance(s) will be created in"
        default = "subnet-08bab56434ab9f549"
}

variable "ami_id" {
        description = "The AMI to use"
        default = "ami-00029538454cd2a00"
}

variable "iam_role" {
    description = "IAM"
    default = "ssm_access"
}

variable "number_of_instances" {
        description = "number of instances to be created"
        default = 1
}


variable "ami_key_pair_name" {
        default = "tomcat"
}
