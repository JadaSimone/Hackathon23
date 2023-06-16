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
    for record in event['Records']: # loop so we can have a multiple kick off in one upload
        bucket = record['s3']['bucket']['name']
        obj_name = record['s3']['object']['key']
        s3_input = "s3://{}/{}".format(bucket, obj_name)
        print("new input: {}".format(s3_input))
    
        #clone(GIT_REPO)
        #install_terraform(TERRAFORM_PATH)
        #apply_terraform_plan()
        
def check_call(args):
    """Wrapper for subprocess that checks if a process runs correctly,
    and if not, prints stdout and stderr.
    """
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd='/tmp')
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        print(stdout)
        print(stderr)
        raise subprocess.CalledProcessError(
            returncode=proc.returncode,
            cmd=args)

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

def apply_terraform_plan():
    os.chdir(CLONE_TO_DIR + '/terraform')
    check_call([TERRAFORM_PATH, '--version'])
    check_call([TERRAFORM_PATH, 'init','-input=false'])
    check_call([TERRAFORM_PATH, 'apply', '/tmp/xmarksspot'])
    # check_call(['terraform', 'apply', '--approve'])

def clone(repoName):
    print('empty the directory')
    files = glob.glob(CLONE_TO_DIR)
    for f in files:
        os.remove(f)
    try:
        shutil.rmtree(CLONE_TO_DIR)
    except:
        pass
    
    print(f'Cloning repo: {repoName}')
    check_call(['git', 'clone', repoName, CLONE_TO_DIR])
