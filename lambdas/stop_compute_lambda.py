import boto3
COMMAND = 'touch /opt/hackathon/test.sh'
#COMMAND = '/opt/hackathon/stop.sh'

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm', region_name='us-east-1')
    instance_id = 'i-01762e272a68629a4' # TODO: get this from the terraform file
    
    print('running command {} on ec2 instance {}'.format(COMMAND, instance_id))
    response = ssm_client.send_command( InstanceIds=[instance_id], DocumentName='AWS-RunShellScript', Parameters={'commands': [COMMAND]})
