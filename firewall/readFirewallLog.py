# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# readFirewallLog.py

import os
import time
import datetime

def main():

    # initialize cooldown variable
    printCooldown = 1 # cooldown in between print statements

    # open log files
    firewallLog = open("../firewall/firewall.log", "r") # open firewall.log for reading
    firewallLogTxt = open("../firewall/firewallLog.txt", "w") # open firewallLog.txt for writing
    currentFirewallLogTxt = open("../firewall/currentFirewallLog.txt", "w") # open currentFirewallLog.txt for writing

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

    warnings = [] # initialize empty array for warnings

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

    # print warnings if any
    print ("|==============================|") # print to terminal
    print ("Warnings from today:") # print to terminal
    if not warnings: # if warnings array is empty
        print("Nothing to report") # print to terminal
    for warning in warnings: # iterate through warnings
        print(warning) # print to terminal
    print ("|==============================|") # print to terminal
    time.sleep(printCooldown)

main()
