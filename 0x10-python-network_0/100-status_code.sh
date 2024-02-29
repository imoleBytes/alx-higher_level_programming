#!/bin/bash
# Bash script to get the status code from the header
curl -sI "$1" | grep HTTP | cut -d " " -f 2
