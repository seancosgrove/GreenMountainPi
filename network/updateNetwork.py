# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# updateNetwork.py

import os
import time

def main():

    # initialize cooldown in between commands
    cmdCooldown = 3
    printCooldown = 1

    # get connected inet address for print message
    networkTxt = open("../network/network.txt","r") # open network.txt file
    inet = networkTxt.read() # read file into string
    inet = inet.strip() # strip whitespace

    # initialize command strings to run python
    IPcmd = "python3 ../network/IP.py"
    nmapCmd = "python3 ../network/nmap.py"

    # execute IP.py
    print("Scanning for networks...")
    time.sleep(printCooldown)
    print("|==============================|")
    os.system(IPcmd)
    print("|==============================|")
    print("Networks located.")
    time.sleep(printCooldown)
    time.sleep(cmdCooldown) # command cooldown

    # execute nmap.py
    print("Executing nmap scan for " + inet + "...")
    time.sleep(printCooldown)
    print("|==============================|")
    os.system(nmapCmd)
    print("|==============================|")
    print("Finished nmap scan.") # build success
    time.sleep(printCooldown)

main()

