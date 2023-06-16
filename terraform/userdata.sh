#! /bin/bash
yum -y install svn git jq
pip3 install boto3
          
mkdir /opt/hackathon/
cd /opt/hackathon/
            
svn export https://github.com/JadaSimone/Hackathon23/trunk/ec2_scripts
mv /opt/hackathon/ec2_scripts/* /opt/hackathon/
chmod +x /opt/hackathon/start.sh
chmod +x /opt/hackathon/stop.sh
input_file=https://raw.githubusercontent.com/JadaSimone/Hackathon23/main/examples/counter/input.json # TODO : pass this in from terraform. don't hard code
curl --url $input_file > input.json

/opt/hackathon/start.sh
