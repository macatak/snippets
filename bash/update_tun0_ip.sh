#!/usr/bin/bash

<<COMMENT
Script to update other files with a new IP
tun0 is the HTB IP in ifconfig
It may change when reconnecting so this is an easy way to update all of the 
files in a folder with the new IP
requires an existing file, current_ip.txt, which should only need to be created the
first time it is run
!!!!
All path names will need to updated for the target machine
!!!!
COMMENT

# get the current tun0 ip
new_tun_ip=$(ifconfig tun0 | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d:)
# get the olf tun0 ip
old_tun_ip=$( cat /home/bikeride/htb/cybernetics/shell/test/current_ip.txt )

# echo "old tun0 ip : $old_tun_ip"
# echo "new tun0 ip : $new_tun_ip"

for file in "/home/bikeride/htb/cybernetics/shell/test"/*
do
  # echo "$file"
  sed -i  "s/$old_tun_ip/$new_tun_ip/g" $file
done
