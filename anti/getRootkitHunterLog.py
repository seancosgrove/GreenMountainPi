# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# getRootkitHunterLog.py

import os
import time

def main():

    # initialize cooldown variable
    cmdCooldown = 3 # cooldown in between os commands

    # copy contents of rkhunter.log to this directory
    antiCmd = "cp -r ~/../../var/log/rkhunter.log ../anti/rkhunter.log" # prepare os command
    os.system(antiCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown

main()
