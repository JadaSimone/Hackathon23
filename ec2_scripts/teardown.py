# trigger lambda to run terraform destroy
import boto3
import subprocess
import json
import os
requestId = os.environ.get('REQUEST_ID','')
print("tearing down requestId: {}".format(requestId))

# topic name should be specific per input & only terminate that one deployment
lambda_client = boto3.client('lambda',region_name='us-east-1')
lambda_payload = {'requestID':requestId}
lambda_client.invoke(FunctionName='terraform_destroy_lambda',
                     InvocationType='Event',
                     Payload=json.dumps(lambda_payload))

subprocess.run(['/opt/hackathon/ec2_scripts/stop.sh'],shell=True)
