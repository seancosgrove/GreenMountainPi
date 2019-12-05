# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# readFirewallLog.py

import os
import datetime

def main():

    # open firewall.log and firewallLog.txt file
    firewallLog = open("../firewall/firewall.log", "r")
    firewallLogTxt = open("../firewall/firewallLog.txt", "w")
    currentFirewallLogTxt = open("../firewall/currentFirewallLog.txt", "w")

    # initialize today's date
    today = datetime.datetime.now() # get today's date
    date = today.strftime("%b-%d-%Y") # format date into string
    date = date.split("-") # split string into list
    month = date[0] # get the month
    day = date[1] # get the day of the month
    day = int(day) # convert day to int for if statement
    if (day < 10): # day is a single digit
        day = str(day) # convert day back to str for date string
        date = month + "  " + day # prepare string to get today's logs (Jan  1)
    else:
        day = str(day) # convert day back to str for date string
        date = month + " " + day # prepare string to get today's logs(Jan 21)

    warnings = []

    # read each line of firewall.log
    for line in reversed(list(firewallLog)):
        log = line.strip() # remove whitespace
        log = log.split("]") # split string into list
        if (len(log) > 1): # log isn't just a timestamp
            timestamp = log[0] # initialize timestamp string
            message = log[1] # initialize message string
            timestamp = timestamp.split(" [") # split timestamp into list
            timestamp = timestamp[0] # get date and time
            timestamp = timestamp.split("rasp") # split string into list
            timestamp = timestamp[0] # get timestamp before "raspberrypi kernal: "
            timestamp = timestamp.strip() # remove whitespace
            message = message.split("kernel: ") # split message into list
            message = message[0] # get message after "raspberrypi kernal: "
            message = message.strip() # remove whitespace
            logLine = timestamp + " " + message # prepare string for file write
            firewallLogTxt.write(logLine + "\n") # write shortened log line to file
            if (timestamp.startswith(date)): # get log lines from today
                currentFirewallLogTxt.write(logLine + "\n") # write shortened log line to file
            if (timestamp.startswith(date) and message.startswith("WARN")): # get warnings from today
                warnings.append(logLine) # append warnings to list

    print ("|==============================|")
    print ("Warnings from today:")
    if not warnings:
        print("Nothing to report")
    for warning in warnings:
        print(warning)
    print ("|==============================|")

main()
