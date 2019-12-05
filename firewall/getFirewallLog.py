# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# getFirewallLog.py

import os
import time

def main():

    # initialize cooldown variable
    cmdCooldown = 3 # cooldown in between os commands

    # copy contents of firewall.log to this directory
    firewallCmd = "cp -r ~/../../var/log/firewall.log ../firewall/firewall.log" # prepare os command
    os.system(firewallCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown

main()

