#!/bin/bash
#This script is to  takes in a URL as an argument, sends a GET request
curl -sSLX GET "{$1}" -H "X-School-User-Id: 98"
