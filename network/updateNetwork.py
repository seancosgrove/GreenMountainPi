# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# updateNetwork.py

import os
import time

def main():

    # initialize cooldown variables
    cmdCooldown = 3 # cooldown in between os commands
    printCooldown = 1 # cooldown in between print statements

    # get connected inet address
    networkTxt = open("../network/network.txt","r") # open network.txt file
    inet = networkTxt.read() # read file into string
    inet = inet.strip() # strip whitespace

    # execute IP.py
    IPpy = "../network/IP.py" # get path to IP.py
    IPcmd = "python3 " + IPpy # prepare os command
    print("Scanning for networks...") # print to terminal
    time.sleep(printCooldown) # print cooldown
    print("|==============================|") # print to terminal
    os.system(IPcmd) # run os command
    time.sleep(cmdCooldown) # command cooldown
    print("|==============================|") # print to terminal
    print("Networks located") # print to terminal
    time.sleep(printCooldown) # print cooldown

    # execute nmap.py
    nmapPy = "../network/nmap.py" # get path to nmap.py
    nmapCmd = "python3 " + nmapPy # prepare os command
    print("Executing nmap scan for " + inet + "...") # print to terminal
    time.sleep(printCooldown) # print cooldown
    print("|==============================|") # print to terminal
    os.system(nmapCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown
    print("|==============================|") # print to terminal
    print("Finished nmap scan") # print to terminal
    time.sleep(printCooldown) # print cooldown

    # execute readNmap.py
    readNmapPy = "../network/readNmap.py" # get path to readNmap.py
    readNmapCmd = "python3 " + readNmapPy # prepare os command
    print("Reading to nmapCaptureLog.txt and nmapScanLog.txt...") # print to terminal
    time.sleep(printCooldown) # print cooldown
    os.system(readNmapCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown
    print("Finished writing to log text files") # build success
    time.sleep(printCooldown) # print cooldown

main()

