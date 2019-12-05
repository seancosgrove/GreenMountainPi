# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# readFirewallLog.py

import os
import datetime

def main():

    # open firewall.log and firewallLog.txt file
    rootkitHunterLog = open("../anti/rkhunter.log", "r")
    rootkitHunterLogTxt = open("../anti/rootkitHunterLog.txt", "w")

    warnings = []

    # read each line of rkhunter.log
    for line in rootkitHunterLog:
        log = line.strip() # remove whitespace
        log = log.split("] ") # split string into list
        if (len(log) > 1): # log isn't just a timestamp
            timestamp = log[0] # initialize timestamp string
            message = log[1] # initialize message string
            logLine = message.strip() # remove whitespace
            rootkitHunterLogTxt.write(logLine + "\n") # write shortened log line to file

    print ("|==============================|")
    print ("Warnings from last scan:")
    if not warnings:
        print("Nothing to report")
    for warning in warnings:
        print(warning)
    print ("|==============================|")

main()
