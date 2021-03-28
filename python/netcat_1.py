#!/usr/bin/python3

'''
Listen for a local TCP connection on port 1233
'''

import nclib


help(nclib.Netcat)
logfile = open('log.txt', 'wb')
nc = nclib.Netcat(listen=('localhost', 1234), log_send=logfile, log_recv=logfile)
nc.interact()
