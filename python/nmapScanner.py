#!/usr/bin/python3

'''
Generic Nmap scanner with arguments
outputs it in CSV format
'''

import csv, nmap

# never hurts to look at the docs
#help(nmap.PortScanner)

nm_scan = nmap.PortScanner()
# this is the scanme.nmap.org IP
target_ip = '45.33.32.156'
# scan command
nm_scan.scan(str(target_ip),  ports='22,80,53,110,143-4564,31337', arguments='-sT -sV')
# print the nmap command line used
print(nm_scan.command_line())

# print the results in CSV format
print(nm_scan.csv())