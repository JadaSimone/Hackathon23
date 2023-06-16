provider "aws" {
    access_key = "${var.access_key}"
    secret_key = "${var.secret_key}"
    region = "us-east-1"
}

# ec2 instance
resource "aws_instance" "ec2_instance" {
    ami = "${var.ami_id}"
    count = "${var.number_of_instances}"
    subnet_id = "${var.subnet_id}"
    instance_type = "${var.instance_type}"
    key_name = "${var.ami_key_pair_name}"
    iam_instance_profile = "${var.iam_role}"
    associate_public_ip_address = true
    vpc_security_group_ids = ["sg-08bf3b80aeb1612be"]
    user_data = filebase64("${path.module}/userdata.sh")
    tags = {

        "Name": "terraform ec2 test"
    }
} 
# asg

resource "aws_launch_configuration" "x_on_the_spot_template" {
  image_id                    = "${var.ami_id}"
  name                        = "ec2_x_on_the_spot_instance"
  security_groups =       ["sg-08bf3b80aeb1612be"]
  key_name                    = "${var.ami_key_pair_name}"
  iam_instance_profile = "${var.iam_role}"
  instance_type               = "${var.instance_type}"
  associate_public_ip_address = true
  spot_price    = "0.0087"
  enable_monitoring = true
  user_data = filebase64("${path.module}/userdata.sh")
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "x_on_the_spot_asg" {
  desired_capacity     = 1
  max_size             = "1"
  min_size             = "1"
  name                 = "x_on_the_spot_instance"
  vpc_zone_identifier  = ["${var.subnet_id}"]
  launch_configuration = aws_launch_configuration.x_on_the_spot_template.name
}

# lambda 
data "aws_iam_policy_document" "lambda_assume_role_policy"{
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "lambda_role" {  
  name = "lambda-lambdaRole-waf"  
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role_policy.json 
}

data "archive_file" "python_lambda_package" {  
  type = "zip"  
  source_file = "${path.module}/../lambdas/stop_compute_lambda.py" 
  output_path = "nametest.zip"
}

 resource "aws_lambda_function" "test_lambda_function" {
         function_name = "stop_compute_lambda"
         filename      = "nametest.zip"
         source_code_hash = data.archive_file.python_lambda_package.output_base64sha256
         # role          = "arn:aws:iam::914058368716:role/service-role/x_on_the_spot_retry-role-5q3wucrg"
         role = aws_iam_role.lambda_role.arn
         runtime       = "python3.10"
         handler       = "stop_compute_lambda.lambda_handler"
         timeout       = 10
 }

