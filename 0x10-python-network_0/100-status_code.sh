#!/bin/bash
# Uses curl to only display status code of a response
curl -so /dev/null -w "%{http_code}" $1
