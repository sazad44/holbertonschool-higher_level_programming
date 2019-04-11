#!/bin/bash
# Send POST request with the contents of a file
curl -H "Content-Type: application/json" -sX POST -d "@$2" $1
