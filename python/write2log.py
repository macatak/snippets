#!/usr/bin/python3

# write a log file in Python using a datetime stamp

from datetime import datetime

# get the current time and date
now = datetime.now()

# declare the log file
# 'a' is for append, creates it if not there
# addes a line if it is
log_file = open("/tmp/spam.log", "a")

# format it so it is HH:MM:SS-day-month-year
# for a 2 digit year use 'y' instead of 'Y'
dts = now.strftime("%H:%M:%S-%d-%m-%Y")
# ISO 8601 format
iso_dts = now.isoformat()
print('human friendly date : {}'.format(dts))
print('ISO 8601 format : {}'.format(iso_dts))

# create a dummy log entry
log_entry = 'always look on the bright side of life'

# write it to a log
log_file.write(log_entry + ' - ' + dts + '\n')
# ISO format
log_file.write(log_entry + ' - ' + iso_dts + '\n')