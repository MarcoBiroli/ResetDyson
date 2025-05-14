#!/bin/bash

set -e

start_time=$(date +%s)

current_date=$(date +%y%m%d)

env_prefix=resetdyson_$current_date

source ~/miniconda3/bin/activate
conda create -n $env_prefix python=3.11 -y -c anaconda
conda activate $env_prefix

echo "Currently in env $(which python)"

pip install --requirement requirements.txt

end_time=$(date +%s)

elapsed_time=$((end_time - start_time))

elapsed_minutes=$((elapsed_time/60))

echo "Environment $env_prefix was succesfully created in $elapsed_minutes minutes."
