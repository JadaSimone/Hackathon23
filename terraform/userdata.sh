#! /bin/bash
yum -y install svn git
pip3 install boto3
          
mkdir /opt/hackathon/
cd /opt/hackathon/
aws s3 cp ${s3_bucket_path}
            
. /opt/hackathon/env.sh
svn export https://github.com/JadaSimone/Hackathon23/trunk/ec2_scripts
chmod +x /opt/hackathon/ec2_scripts/start.sh
chmod +x /opt/hackathon/ec2_scripts/stop.sh
input_file=https://raw.githubusercontent.com/JadaSimone/Hackathon23/main/examples/counter/input.json # TODO : pass this in from terraform. don't hard code
curl --url $input_file > input.json

/opt/hackathon/ec2_scripts/start.sh
