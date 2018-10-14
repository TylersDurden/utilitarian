#!/bin/bash
cd $1
ls | while read file; do
    echo "Deleting "$file
    file=$file
    rm -- *\ * && rm $1/$file
done;
cd ..
rmdir $1
#EOF
