#!/bin/sh
echo 'Which device do you want to tap into?:'
i=0
lsblk | while read line; do echo '['$i'] -  '$line;i=$((i+1)); done
read choice
opt=0
case $choice in
	1) opt=1 ;;
	2) opt=2 ;;
	3) opt=3 ;;
	4) opt=4 ;;
	5) opt=5 ;;
	6) opt=6 ;;
	7) opt=7 ;;
        8) opt=8 ;;
        9) opt=10 ;;	
        *) echo 'Invalid Selection!';;
esac
echo 'Tapping:'
j=0
lsblk | while read name; do 
    if [ $j -eq $opt ]; then
        echo $name;
    fi
    j=$((j+1))
done
#EOF
