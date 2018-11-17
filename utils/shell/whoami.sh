#!/bin/bash
ifconfig wlan0 | perl -nle'/(\d+\.\d+\.\d+\.\d+)/ && print $1'
#EOF
