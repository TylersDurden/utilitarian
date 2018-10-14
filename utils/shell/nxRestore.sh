#!/bin/bash
rfkill unblock 1
ifconfig wlan0 up
iwlist wlan0 scan | grep "Cell"
iwlist wlan0 scan | grep "ESSID"
echo 'Enter your network name: '
read nxname
iwconfig wlan0 essid $nxname
iw dev wlan0 connect $nxname

