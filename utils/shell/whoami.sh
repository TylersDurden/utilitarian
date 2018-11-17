#!/bin/bash
ifconfig wlan0 | perl -nle'/(\d+\.\d+\.\d+\.\d+)/ && print $1'
iwconfig wlan0 | grep 'ESSID:' | sed 's/wlan0     IEEE 802.11/\n/g' | sed 's/ESSID:/\n/g'
#EOF
