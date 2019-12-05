# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# nmap.py

import os
import time

def main():

    # initialize cooldown variables
    cmdCooldown = 3 # cooldown in between os commands
    printCooldown = 1 # cooldown in between print statements

    # get connected inet address
    networkTxt = open("../network/network.txt","r") # open network.txt file
    inet = networkTxt.read() # read file into string
    inet = inet.strip() # remove whitespace

    # execute basic nmap scan of inet and http server
    nmapCaptureCmd = ("nmap --script=http-title -oN ../network/nmapCapture.txt " + inet) # prepare os command
    os.system (nmapCaptureCmd) # execute os command
    time.sleep (cmdCooldown) # command cooldown
    print("|==============================|") # print to terminal
    time.sleep(printCooldown) # print cooldown

    # execute nmap scan of UDP ports to look for DDOS vulnerabilities
    print("Scanning UDP ports for possible DDOS attacks...") # print to terminal
    print("|==============================|") # print to terminal
    nmapScanCmd = ("nmap -sU -A -PN -n -pU:19,53,123,161 -script=ntp-monlist,dns-recursion,snmp-sysdescr -oN ../network/nmapScan.txt " + inet) # prepare os command
    os.system (nmapScanCmd) # execute os command
    time.sleep(cmdCooldown) # command cooldown

main()
