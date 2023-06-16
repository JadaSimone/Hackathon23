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

GITHUB_REPO = f"https://github.com/JadaSimone/Hackathon23.git"
CLONE_LOCATION = '/tmp/xmarksspot'

def lambda_handler(event, context):
    clone(GITHUB_REPO)
    install_terraform()
    apply_terraform_plan()
    
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

def install_terraform():
    """Install Terraform on the Lambda instance."""
    # Most of a Lambda's disk is read-only, but some transient storage is
    # provided in /tmp, so we install Terraform here.  This storage may
    # persist between invocations, so we skip downloading a new version if
    # it already exists.
    # http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction.html
    print(TERRAFORM_PATH)
    
    if os.path.exists(TERRAFORM_PATH):
        return
    
    urllib.request.urlretrieve(TERRAFORM_DOWNLOAD_URL, '/tmp/terraform.zip')
    print('downloaded terraform')
    # Flags:
    #   '-o' = overwrite existing files without prompting
    #   '-d' = output directory
    check_call(['unzip', '-o', '/tmp/terraform.zip', '-d', TERRAFORM_DIR])
    check_call([TERRAFORM_PATH, '--version'])

def apply_terraform_plan():
    os.chdir(CLONE_LOCATION)
    #os.system('terraform plan'))
    check_call([TERRAFORM_PATH, '--version'])
    check_call([TERRAFORM_PATH, 'init','-input=false'])
    check_call([TERRAFORM_PATH, 'apply', CLONE_LOCATION])
    # check_call(['terraform', 'apply', '--approve'])

def clone(repoUrl):
    print('empty the directory')
    files = glob.glob(CLONE_LOCATION)
    for f in files:
        os.remove(f)
    try:
        shutil.rmtree(localDir)
    except:
        pass
    print('cloning repo')
    check_call(['git', 'clone', repoUrl, CLONE_LOCATION])
    #localRepo = Repo.clone_from(repoUrl, CLONE_LOCATION)
    print(f'Cloned repo: {repoName}')
    
