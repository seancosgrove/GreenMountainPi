# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# updateFirewall.py

import os
import time

def main():

    # initialize cooldown in between commands
    cmdCooldown = 3

    # initialize command strings to run python
    getFirewallLogCmd = "python3 getFirewallLog.py"
    readFirewallLogCmd = "python3 readFirewallLog.py"

    # execute getFirewallLog.py
    print("Getting firewall.log...")
    os.system(getFirewallLogCmd)

    time.sleep(cmdCooldown) # command cooldown

    # execute readFirewallLog.py
    print("Reading to firewallLog.txt...")
    os.system(readFirewallLogCmd)

    print("Done.") # build success

main()
