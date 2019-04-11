#!/bin/bash
# Request catch_me resource path of 0:5000 and get You got me! message
curl -sLH "Origin: HolbertonSchool" -d "user_id=98" -X PUT 0:5000/catch_me
