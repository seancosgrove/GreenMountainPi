# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# readRootkitHunterLog.py

import os
import time

def main():

    # initialize cooldown variable
    printCooldown = 1 # cooldown in between print statements

    # open log files
    rootkitHunterLog = open("../anti/rkhunter.log", "r") # open rkhunter.log
    rootkitHunterLogTxt = open("../anti/rootkitHunterLog.txt", "w") # open rookitHunterLog.txt
    rootkitHunterLogWarnings = open("../anti/rootkitHunterLogWarnings.txt", "w") # open rootkitHunterLogWarnings.txt

    warnings = [] # initialize empty array for warnings

    # read each line of rkhunter.log
    for line in rootkitHunterLog:
        log = line.strip() # remove whitespace
        log = log.split("] ") # split string into list
        if (len(log) > 1): # log isn't just a timestamp
            timestamp = log[0] # initialize timestamp string
            message = log[1] # initialize message string
            logLine = message.strip() # remove whitespace
            if (logLine.startswith("Info:")):
                logLine = logLine.split("Info: ") # split string into list
                logLine = logLine[1] # get info message from log (log[0] is an empty string)
                logLine = logLine.strip() # remove whitespace
            if (logLine.endswith("[ Warning ]")): # logLine contains a warning
                warnings.append(logLine) # append logLine to wanrings array
                rootkitHunterLogWarnings.write(logLine + "\n") # write log line to warnings file
            rootkitHunterLogTxt.write(logLine + "\n") # write log line to file

    # print warnings if any
    print ("|==============================|") # print to terminal
    print ("Warnings from last scan:") # print to terminal
    if not warnings: # warnings array is empty
        print("Nothing to report") # print to terminal
    for warning in warnings: # iterate through warnings
        print(warning) # print to terminal
    print ("|==============================|") # print to terminal
    time.sleep(printCooldown) # print cooldown

main()
