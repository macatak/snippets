#!/usr/bin/bash

<<COMMENT
use grep return code to determine if a match is found
syntax
grep <search term> <full path to file
# target
"GET /shell.aspx HTTP/1.1" 200 -
COMMENT

grep_test () {
    # printf "$1\n$2"
    grep $1 $2 > /dev/null
    return $?
}

# search_for=200
# search_for="\"GET /shell.aspx HTTP/1.1\" 200 -"
search_for='\"GET /shell.aspx HTTP/1.1\" 200'
printf "$search_for\n"
search_path="/home/bikeride/htb/cybernetics/shell/screenlog.0"
printf "$search_path\n\n"

grep_test $search_for $search_path
if [ $? == 0 ]
then
  printf "match"
else
  printf "no match"
fi
