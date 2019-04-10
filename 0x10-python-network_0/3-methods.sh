#!/bin/bash
# Extracts allowed HTTP operations from response header
curl -sI $1 | grep 'Allow' | awk -v RS='\r\n' -F": " '{ print $2 }'
