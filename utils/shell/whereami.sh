#!/bin/bash
echo '\033[1m\033[35m'"External IP and GeoLocation:"'\033[0m'
echo '\033[1m\033[33m'$(GET https://ipinfo.io/$(GET https://api.ipify.org/))'\033[0m'

#EOF
