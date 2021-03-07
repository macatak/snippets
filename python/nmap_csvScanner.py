#!/usr/bin/python3

'''
Open a CSV file with in the format:
<IP>,<PORT>
example
127.0.0.1,8080
127.0.0.1,443
'''

import csv, nmap

nm_scan = nmap.PortScanner()

with open ('G:\\atom_workspace\\files\\nmap_targets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names : {", ".join(row)}')
            line_count += 1
        elif len(row[1]) != 0:
            target_ip = row[0]
            target_port = row[1]
            # print(len(target_port))
            nm_scan.scan(str(target_ip), target_port)
            port_state = nm_scan[target_ip]['tcp'][int(target_port)]['state']
            print(nm_scan.command_line())
            print('IP: {} Port : {} State {}'.format(target_ip, target_port, port_state))
            line_count += 1
        else:
            print('No port specified')
            line_count += 1                
    print('Processed {} lines'.format(line_count))