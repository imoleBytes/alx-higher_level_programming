#!/bin/bash
# Bash script to get the status code from the header curl -si "$1" | grep HTTP | cut -d " " -f 2
curl -s -o /dev/null -w "%{http_code}" "$1"
