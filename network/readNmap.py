# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# readFirewallLog.py

import os
import time

def main():

    # open log files
    nmapCapture = open("../network/nmapCapture.txt", "r") # open nmapCapture.txt for reading
    nmapScan = open("../network/nmapScan.txt", "r") # open nmapScan.txt for reading
    nmapCaptureLog = open("../network/nmapCaptureLog.txt", "w") # open nmapCaptureLog.txt for writing
    nmapScanLog = open("../network/nmapScanLog.txt", "w") # open nmapScanLog.txt for writing

    # read each line of nmapCature.txt
    for line in (nmapCapture):
        log = line.strip() # remove whitespace
        if (log.startswith("#")):
            log = log.split(" as:") # split string into list
            log = log[0] # get timestamp of log (log[1] = nmap command)
            log = log.strip() # remove whitespace
        if (log.startswith("|")):
            log = log.split("_") # split string into list 
            log = log[1] # get http-title of log (log[0] = "|")
            log = log.strip() # remove whitespace
        nmapCaptureLog.write(log + "\n") # write to nmapCaptureLog.txt

    # read each line of nmapScan.txt
    for line in (nmapScan):
        log = line.strip() # remove whitespace
        if (log.startswith("#")):
            log = log.split(" as:") # split string into list
            log = log[0] # get timestamp of log (log[1] = nmap command)
            log = log.strip() # remove whitespace
        nmapScanLog.write(log + "\n") # write to nmapScanLog.txt

main()
