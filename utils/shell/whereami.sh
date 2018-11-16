#!/bin/bash
GET https://ipinfo.io/$(GET 'https://api.ipify.org?format=json' | jq -r .'ip')
#EOF
