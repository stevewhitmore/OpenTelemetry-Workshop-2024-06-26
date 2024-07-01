#!/bin/bash

cd aspire
docker compose down

function kill_port {
    # Get the PID of the process using TCP port 5000
    pid=$(lsof -wni tcp:$1 | awk 'NR==2 {print $2}')

    # Check if a PID was found
    if [ -n "$pid" ]; then
    # Kill the process
    kill -9 $pid
    echo "Process $pid on port $1 has been killed."
    else
    echo "No process found on port $1."
    fi
}

kill_port 8080
kill_port 5000