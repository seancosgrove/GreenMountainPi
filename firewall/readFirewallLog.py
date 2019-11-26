# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# readFirewallLog.py

import os

def main():

    # open firewall.log and firewallLog.txt file
    firewallLog = open("firewall.log", "r")
    firewallLogTxt = open("firewallLog.txt", "w")

    # read each line of firewall.log
    for line in firewallLog:
        log = line.strip() # remove whitespace
        log = log.split("]") # split string into list
        if (len(log) > 1): # log isn't just a timestamp
            timestamp = log[0] # initialize timestamp string
            message = log[1] # initialize message string
            timestamp = timestamp.split(" [") # split timestamp into list
            timestamp = timestamp[0] # get date and time
            timestamp = timestamp.strip() # remove whitespace
            message = message.strip() # remove whitespace
            logLine = timestamp + " " + message # prepare string for file write
            firewallLogTxt.write(logLine + "\n") # write shortened log line to file

main()
