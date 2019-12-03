# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# readFirewallLog.py

import os
import datetime

def main():

    # open firewall.log and firewallLog.txt file
    firewallLog = open("../firewall/firewall.log", "r")
    firewallLogTxt = open("../firewall/firewallLog.txt", "a")
    currentFirewallLogTxt = open("../firewall/currentFirewallLog.txt", "w")

    # initialize today's date
    today = datetime.datetime.now() # get today's date
    date = today.strftime("%b-%d-%Y") # format date into string
    date = date.split("-") # split string into list
    month = date[0] # get the month
    day = date[1] # get the day of the month
    date = month + " " + day # prepare string to get today's logs

    warnings = []

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
            if (timestamp.startswith(date)): # get log lines from today
                currentFirewallLogTxt.write(logLine + "\n") # write shortened log line to file
            if (timestamp.startswith(date) and message.startswith("WARN")): # get warnings from today
                warnings.append(logLine) # append warnings to list

    for warning in warnings:
        print(warning)

main()