provider "aws" {
    access_key = "${var.access_key}"
    secret_key = "${var.secret_key}"
    region = "us-east-1"
}

#TODO : also create the AMI if we have time
#TODO : create separate terraform file that creates the "terraform_apply_lambda". This one will be built by terraform_apply_lambda
#TODO : in ec2 instance userdata download everything in this repo under ec2_scripts to /opt/hackathon
#TODO : Autoscaling group
#TODO : cloudwatch event rule - used to trigger stop_compute_lambda see https://registry.terraform.io/providers/hashicorp/aws/3.6.0/docs/resources/cloudwatch_event_rule & CloudWatchEventRule in cloudformation here https://github.com/aws-deepracer-community/deepracer-on-the-spot/blob/main/spot-instance.yaml 

resource "aws_instance" "ec2_instance" {
    ami = "${var.ami_id}"
    count = "${var.number_of_instances}"
    subnet_id = "${var.subnet_id}"
    instance_type = "${var.instance_type}"
    key_name = "${var.ami_key_pair_name}"
    iam_instance_profile = "${var.iam_role}"
    associate_public_ip_address = true
    vpc_security_group_ids = ["sg-08bf3b80aeb1612be"]

    tags = {

        "Name": "terraform ec2 test"
    }
} 

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
  assume_role_policy = "arn:aws:iam::aws:policy/AdministratorAccess"
}

data "archive_file" "python_lambda_package" {  
  type = "zip"  
  source_file = "${path.module}/lambda_function.py" 
  output_path = "nametest.zip"
}

# resource "aws_lambda_function" "test_lambda_function" {
#         function_name = "lambdaTest"
#         filename      = "nametest.zip"
#         source_code_hash = data.archive_file.python_lambda_package.output_base64sha256
#         # role          = "arn:aws:iam::914058368716:role/service-role/x_on_the_spot_retry-role-5q3wucrg"
#         role = aws_iam_role.lambda_role.arn
#         runtime       = "python3.10"
#         handler       = "lambda_function.lambda_handler"
#         timeout       = 10
# }