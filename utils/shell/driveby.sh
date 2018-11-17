#!/bin/bash 
lsblk
echo 'Enter the drive you want to explore:'
read drive
echo '/dev/'$drive' Selected'
clear;
udisksctl info -b '/dev/'$drive
#EOF
