# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# updateNetwork.py

import os
import time

def main():

    # initialize cooldown in between commands
    cmdCooldown = 3

    # get connected inet address for print message
    networkTxt = open("network.txt","r") # open network.txt file
    inet = networkTxt.read() # read file into string
    inet = inet.strip() # strip whitespace

    # initialize command strings to run python
    IPcmd = "python3 IP.py"
    nmapCmd = "python3 nmap.py"

    # execute IP.py
    print("Scanning for networks...")
    os.system(IPcmd)

    time.sleep(cmdCooldown) # command cooldown

    # execute nmap.py
    print("Executing nmap scan for " + inet + "...")
    os.system(nmapCmd)

    print("Done.") # build success

main()

