#!/bin/bash

compute=$(jq .compute api_input.json | tr -d "\"")
requirements=$(jq .requirements[] api_input.json | tr -d "\"")
state_store=$(jq .state_store api_input.json)
state_message=$(jq .state_message api_input.json)
s3_state=$(jq .state_store.location api_input.json | tr -d "\"")

# install the requirements
for requirement in $requirements
do
    yum install $requirement
done

# install what we need to compute
curl --url $compute > compute.py
chmod +x compute.py

# check the current state
aws s3 cp $s3_state state.txt
current_state=$(<state.txt)

# start the processes where we left off
python compute.py $current_state
