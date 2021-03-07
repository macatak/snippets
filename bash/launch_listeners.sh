#!/usr/bin/bash

# This is for Kali Linux
# mate-terminal may not be installed
# probably just replace mate-terminal with terminal
#
# Opens a Python HTTP on port 80
# and 2 netcat listeners on 8443 and 8081

# python is at the end since it requires sudo
# and it's easy to forget
mate-terminal --window --geometry=100x25 --tab --title="nc-8443" -e "bash -c \"echo 'nc -lvp 8443';/home/bikeride/htb/cybernetics/shell/nc_8443.sh; exec bash\"" --tab --title="nc-8081" -e "bash -c \"echo 'nc -lvp 8081'; /home/bikeride/htb/cybernetics/shell/nc_8081.sh; exec bash\"" --tab --title="python-80" -e "bash -c \"echo 'sudo python -m SimpleHTTPServer 80'; /home/bikeride/htb/cybernetics/shell/python_80.sh; exec bash\"" 
