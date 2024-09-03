#!/bin/bash

# Check if the user provided a number of iterations
if [ -z "$1" ]; then
    echo "Usage: $0 <number_of_iterations>"
    exit 1
fi

iterations=$1

for i in $(seq 1 $iterations)
do
    # Generate a random seed using /dev/urandom
    seed=$(od -An -N4 -tu4 < /dev/urandom | tr -d ' ')
    echo "Running command $i/$iterations"
    diambra -r ~/.diambra/roms run -l python3 script.py --log.format fancy
    echo "Completed command $i/$iterations."
    echo ""
    sleep 60s
done

echo "All commands executed."
