# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# updateFirewall.py

import os
import time

def main():

    # initialize cooldown variables
    cmdCooldown = 3 # cooldown in between os commands
    printCooldown = 1 # cooldown in between print statements

    # execute getFirewallLog.py
    getFirewallLog = "../firewall/getFirewallLog.py" # get path to getFirewallLog.py
    getFirewallLogCmd = "python3 " + getFirewallLog # prepare os command
    print("Getting firewall.log...") # print to terminal
    time.sleep(printCooldown) # print cooldown
    os.system(getFirewallLogCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown

    # execute readFirewallLog.py
    readFirewallLog = "../firewall/readFirewallLog.py" # get path to readFirewallLog.py
    readFirewallLogCmd = "python3 " + readFirewallLog # prepare os command
    print("Reading to firewallLog.txt and currentFirewallLog.txt...")  # print to terminal
    time.sleep(printCooldown) # print cooldown
    os.system(readFirewallLogCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown
    print("Finished writing to log text files") # build success
    time.sleep(printCooldown) # print cooldown

main()
