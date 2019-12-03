# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# updateFirewall.py

import os
import time

def main():

    # initialize cooldown in between commands
    cmdCooldown = 3
    printCooldown = 1

    # initialize command strings to run python
    getFirewallLogCmd = "sudo python3 ../firewall/getFirewallLog.py"
    readFirewallLogCmd = "sudo python3 ../firewall/readFirewallLog.py"

    # execute getFirewallLog.py
    print("Getting firewall.log...")
    time.sleep(printCooldown)
    os.system(getFirewallLogCmd)
    time.sleep(cmdCooldown) # command cooldown

    # execute readFirewallLog.py
    print("Reading to firewallLog.txt and currentFirewallLog.txt...")
    time.sleep(printCooldown)
    os.system(readFirewallLogCmd)
    time.sleep(cmdCooldown)
    print("Finished writing to log text files") # build success
    time.sleep(printCooldown)

main()
