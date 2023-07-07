#!/bin/bash
#This script is to send a request to a url and print the no of outputed lines
curl -sS "{$1}" | wc -c
