Bash scripts

  - launch_listeners is a script that opens a terminal window with 4 tabs: 1 regular, 2 Netcat tabs with listeners on 8443 and 8081, and a Python web server on port 80. Those scripts are all uploaded as well
  - update_tun0_ip.sh - updates all the files in the target directory with a new tun0 IP. Useful because sometimes when you reconnect to a VPN server, like HTB, the tun0 IP may change and sometimes there are scripts that use that IP.
