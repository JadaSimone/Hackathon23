#!/bin/bash

compute=$(jq .compute input.json | tr -d "\"")
requirements=$(jq .requirements[] input.json | tr -d "\"")
s3_state=$(jq .state_store.location input.json | tr -d "\"")

# install the requirements
for requirement in $requirements
do
    yum install $requirement
done

# install what we need to compute
curl --url $compute > compute.py

# check the current state
aws s3 cp $s3_state state.txt
if [ -f "state.txt" ]; then
    current_state=$(<state.txt)
    # start the processes where we left off
    python compute.py $current_state
else
    python compute.py
fi
