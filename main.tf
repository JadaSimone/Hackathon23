provider "aws" {
    access_key = "${var.access_key}"
    secret_key = "${var.secret_key}"
    region = "us-east-1"
}

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



resource "aws_internet_gateway" "some_ig" {
  vpc_id = "vpc-0532566621291c7b6"

  tags = {
    Name = "Some Internet Gateway"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = "vpc-0532566621291c7b6"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.some_ig.id
  }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id      = aws_internet_gateway.some_ig.id
  }

  tags = {
    Name = "Public Route Table"
  }
}

resource "aws_route_table_association" "public_1_rt_a" {
  subnet_id      = "subnet-08bab56434ab9f549"
  route_table_id = aws_route_table.public_rt.id
}