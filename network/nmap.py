# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# nmap.py

import os

def main():

    os.system ('hostname -I')
    os.system ('nmap -oN nmapcapture.txt 192.168.1.23')

main()
