#!/bin/bash
echo '!ReverseReverse!'
addrs=$(echo $(host $1) | sed 's/in-addr.arpa domain name pointer /\n/g')
echo $addrs | sed 's/ /\n/g'
#EOF
