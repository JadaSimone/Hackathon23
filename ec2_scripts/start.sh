#!/bin/bash

compute=$(jq .compute input.json | tr -d "\"")
requirements=$(jq .requirements[] input.json | tr -d "\"")
s3_state=$(jq .state_store.location input.json | tr -d "\"")
state_save=$(jq .state_save input.json | tr -d "\"")

# install the requirements
for requirement in $requirements
do
    yum install $requirement # TODO: don't assume we are yum installing everything in requirements. We may just want to exec everything in requirements
done

# install what we need to compute
curl --url $compute > compute.py
curl --url $state_save > state_save.py

# check the current state
aws s3 cp $s3_state state.txt
if [ -f "state.txt" ]; then
    current_state=$(<state.txt)
    # start the processes where we left off
    python3 compute.py $current_state
else
    python3 compute.py
fi
python3 teardown.py
