#!/bin/bash 
p=$PWD;
cd /; find -name *$1 | cut -b 2- >> out.txt;
mv out.txt $p; cd $p; 
cat out.txt
#EOF
