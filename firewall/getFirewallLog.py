# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# getFirewallLog.py

import os

def main():

    # copy contents of firewall.log to this directory
    firewallCmd = "sudo cp -r ~/../../var/log/firewall.log ../firewall/firewall.log"
    os.system(firewallCmd)

main()

