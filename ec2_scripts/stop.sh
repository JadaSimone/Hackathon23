#!/bin/bash
echo "stopping compute."
state_measure=$(jq .state_measure api_input.json | tr -d "\"")
s3_state_upload=$(jq .state_store.location api_input.json | tr -d "\"")

# measure state
curl --url $state_measure > state_measure.py
echo $(python3 state_measure.py) > state.txt

# upload state
aws s3 cp state.txt $s3_state_upload

# stop process
# shutdown -h now
