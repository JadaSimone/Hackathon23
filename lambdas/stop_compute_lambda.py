import boto3
COMMAND = '/opt/hackathon/stop.sh'

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm', region_name='us-east-1')
    print(event)
    
    instance_id = event['detail']['instance-id']
    
    print('running command {} on ec2 instance {}'.format(COMMAND, instance_id))
    response = ssm_client.send_command( InstanceIds=[instance_id], DocumentName='AWS-RunShellScript', Parameters={'commands': [COMMAND]})
