# sends a messages to SNS to run terraform destroy 
import boto3

client = boto3.get_client('sns')
# topic name should be specific per input & only terminate that one deployment
client.publish(TopicArn='TBD', Message=f'tear down infrastructure')
