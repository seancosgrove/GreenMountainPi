# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# nmap.py

import os

def main():

    # run nmap os command with connected network inet
    networkTxt = open("../network/network.txt","r") # open network.txt file with connected network inet
    inet = networkTxt.read() # read file into string
    cmd = ("nmap --script=http-title -oN ../network/nmapCapture.txt " + inet) # create string for os command
    os.system (cmd) # execute os command
    print("|==============================|")
    print("Scanning UDP ports for possible DDOS attacks...")
    print("|==============================|")
    cmd2 = ("nmap -sU -A -PN -n -pU:19,53,123,161 -script=ntp-monlist,dns-recursion,snmp-sysdescr -oN ../network/nmapScan.txt " + inet)
    os.system (cmd2)

main()
