#!/bin/bash
# Retrieving the size of the body of the response of a request

curl -sw "\n%{size_download}\n" $1 | tail -1
