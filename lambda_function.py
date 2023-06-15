import json
import boto3
    
def lambda_handler(event, context):
    ssm_client = boto3.client('ssm', region_name='us-east-1')
    print('client made {}'.format(ssm_client))
    instance_id = 'i-01762e272a68629a4'
    response = ssm_client.send_command( InstanceIds=[instance_id], DocumentName="AWS-RunShellScript", Parameters={'commands': ['touch /opt/hackathon/test.sh']})
