#!/usr/bin/python3

from subprocess import Popen, PIPE
import subprocess

# this outputs to the screen some text but then this:
# print(python_8080.stdout.readlines())
# can be searched
python_8080 = subprocess.Popen(["nohup", "python", "-m", "SimpleHTTPServer", "8080"], stdout=PIPE)
#
# this would require manual interaction to see if the file was pulled
# python_8080 = subprocess.Popen(["python", "-m", "SimpleHTTPServer", "8080"], stdout=PIPE)
# 

input("press a key to kill the process\n")
python_8080.terminate()


print(python_8080.stdout.readlines())
