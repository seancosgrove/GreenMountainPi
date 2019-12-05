# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# getRootkitHunterLog.py

import os

def main():

    # copy contents of rkhunter.log to this directory
    antiCmd = "sudo cp -r ~/../../var/log/rkhunter.log ../anti/rkhunter.log"
    os.system(antiCmd)

main()
