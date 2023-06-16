#! /bin/bash
yum -y install svn git
pip3 install boto3
          
mkdir /opt/hackathon/
cd /opt/hackathon/
aws s3 cp ${s3_bucket_path}
echo "REQUEST_ID=${var.request_id}" | sudo tee -a /opt/hackathon/env.sh
            
. /opt/hackathon/env.sh
svn export https://github.com/JadaSimone/Hackathon23/trunk/ec2_scripts
chmod +x /opt/hackathon/ec2_scripts/start.sh
chmod +x /opt/hackathon/ec2_scripts/stop.sh
/opt/hackathon/ec2_scripts/start.sh
