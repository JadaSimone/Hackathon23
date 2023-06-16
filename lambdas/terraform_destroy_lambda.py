# -*- coding: utf-8 -*-

import os
import subprocess
import urllib
import boto3
import os
import glob

TERRAFORM_VERSION = '0.8.5'
# Download URL for Terraform
TERRAFORM_DOWNLOAD_URL = (
'https://releases.hashicorp.com/terraform/%s/terraform_%s_linux_amd64.zip'
% (TERRAFORM_VERSION, TERRAFORM_VERSION))

# Paths where Terraform should be installed
TERRAFORM_DIR = os.path.join('/tmp', 'terraform_%s' % TERRAFORM_VERSION)
TERRAFORM_PATH = os.path.join(TERRAFORM_DIR, 'terraform')

GIT_REPO = "https://github.com/JadaSimone/Hackathon23.git"
CLONE_TO_DIR = "/tmp/xmarksspot"

def lambda_handler(event, context):
      print("TODO: catch event and parse to see which instance/resources we should tear down")
      #clone(GIT_REPO)
      #install_terraform(TERRAFORM_PATH)
      #apply_terraform_destroy()

def install_terraform(path):
    """Install Terraform on the Lambda instance."""
    # Most of a Lambda's disk is read-only, but some transient storage is
    # provided in /tmp, so we install Terraform here.  This storage may
    # persist between invocations, so we skip downloading a new version if
    # it already exists.
    # http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction.html
    print(path)
    
    if os.path.exists(path):
        return
    
    urllib.request.urlretrieve(TERRAFORM_DOWNLOAD_URL, '/tmp/terraform.zip')
    print('downloaded terraform')
    # Flags:
    #   '-o' = overwrite existing files without prompting
    #   '-d' = output directory
    check_call(['unzip', '-o', '/tmp/terraform.zip', '-d', TERRAFORM_DIR])

    check_call([path, '--version'])

def apply_terraform_destroy():
    terraform_path = TERRAFORM_PATH + '/terraform'
    os.chdir(terraform_path)
    check_call([TERRAFORM_PATH, '--version'])
    check_call([TERRAFORM_PATH, 'init','-input=false'])
    check_call([TERRAFORM_PATH, 'destroy', terraform_path])
