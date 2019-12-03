# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# nmap.py

import os

def main():

    # run nmap os command with connected network inet
    networkTxt = open("/var/www/network/network.txt","r") # open network.txt file with connected network inet
    inet = networkTxt.read() # read file into string
    cmd = ("nmap -oN /var/www/network/nmapCapture.txt " + inet) # create string for os command
    os.system (cmd) # execute os command

main()
