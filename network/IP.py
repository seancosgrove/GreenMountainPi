# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# IP.py

import os

def main():

    # open IP.txt file
    IPtxt = open("IP.txt", "w")
    networkTxt = open("network.txt", "w")

    # initialize variables
    eth0 = " "
    lo = " "
    wlan0 = " "

    # read contents of 'ifconfig' os command to a string
    ifconfig = os.popen('ifconfig').read()
    # split contents of ifconfig string into a list
    ifconfig = ifconfig.split('\n')
    # iterate through each line of ifconfig list
    for line in ifconfig:

        # wlan0 network
        if line.startswith('wlan0'):
            os.system('echo "WLAN0 LOCATED"') # console echo that wlan0 was found
            id = ifconfig.index(line) # get list index of first line with 'wlan0'
            inetid = id + 1 # get list index of next line with inet address
            inet = ifconfig[inetid] # get inet address line with index number
            inet = inet.strip() # strip whitespace
            inet = inet.split() # split inet address line into a list
            inet = inet[1] # get index 1 of inet address list (0 = "inet:", 1 = "1.1.1.1.1")
            wlan0 = inet # set wlan0 variable equal to the inet address
            # read contents of 'iwgetid wlan0' os command to a string
            iwgetid = os.popen('iwgetid wlan0').read()
            if iwgetid.startswith('wlan0'): # iwgetid string is not empty (connected to this network)
                iwgetid = iwgetid.split() # split contents of iwgetid string into a list
                ESSID = iwgetid[1] # get index 1 of iwgetid list (0 = "etho", 1 = "ESSID: 'Network Name'")
                ESSID = ESSID.split('"') # split ESSID string into a list to get ride of quotations
                ESSID = ESSID[1] # get index 1 of ESSID list (0 = "ESSID: ", 1 = "Network Name")
                wlan0Network = "wlan0: " + inet + " | ESSID: " + ESSID # store network inet and ESSID in a string
                print(wlan0Network) # print wlan0 network string
                wlan0 = wlan0Network # store wlan0 network string as global wlan0 variable
                networkTxt.write(inet) # write inet of connected network to network.txt
            else: # iwgetid string is empty
                wlan0Network = "wlan0: " + inet # store network inet in a string
                print(wlan0Network) # print wlan0 network string
                wlan0 = wlan0Network # store wlan0 network string as global wlan0 variable

        # eth0 network
        if line.startswith('eth0'):
            os.system('echo "ETH0 LOCATED"') # console echo that eth0 was found
            id = ifconfig.index(line) # get list index of first line with 'eth0'
            inetid = id + 1 # get list index of next line with inet address
            inet = ifconfig[inetid] # get inet address line with index number
            inet = inet.strip() # strip whitespace
            inet = inet.split() # split inet address line into a list
            inet = inet[1] # get index 1 of inet address list (0 = "inet:", 1 = "1.1.1.1.1")
            eth0 = inet # set eth0 variable equal to the inet address
            # read contents of 'iwgetid eth0' os command to a string
            iwgetid = os.popen('iwgetid eth0').read()
            if iwgetid.startswith('eth0'): # iwgetid string is not empty (connected to this network)
                iwgetid = iwgetid.split() # split contents of iwgetid string into a list
                ESSID = iwgetid[1] # get index 1 of iwgetid list (0 = "etho", 1 = "ESSID: 'Network Name'")
                ESSID = ESSID.split('"') # split ESSID string into a list to get ride of quotations
                ESSID = ESSID[1] # get index 1 of ESSID list (0 = "ESSID: ", 1 = "Network Name")
                eth0Network = "eth0: " + inet + " | ESSID: " + ESSID # store network inet and ESSID in a string
                print(eth0Network) # print eth0 network string
                eth0 = eth0Network # store eth0 network string as global eth0 variable
                networkTxt.write(inet) # write inet of connected network to network.txt
            else: # iwgetid string is empty
                eth0Network = "eth0: " + inet # store network inet in a string
                print(eth0Network) # print eth0 network string
                eth0 = eth0Network # store eth0 network string as global eth0 variable

        # lo network
        if line.startswith('lo'):
            os.system('echo "LO LOCATED"') # console echo that lo was found
            id = ifconfig.index(line) # get list index of first line with 'lo'
            inetid = id + 1 # get list index of next line with inet address
            inet = ifconfig[inetid] # get inet address line with index number
            inet = inet.strip() # strip whitespace
            inet = inet.split() # split inet address line into a list
            inet = inet[1] # get index 1 of inet address list (0 = "inet:", 1 = "1.1.1.1.1")
            lo = inet # set lo variable equal to the inet address
            # read contents of 'iwgetid lo' os command to a string
            iwgetid = os.popen('iwgetid lo').read()
            if iwgetid.startswith('lo'): # iwgetid string is not empty (connected to this network)
                iwgetid = iwgetid.split() # split contents of iwgetid string into a list
                ESSID = iwgetid[1] # get index 1 of iwgetid list (0 = "etho", 1 = "ESSID: 'Network Name'")
                ESSID = ESSID.split('"') # split ESSID string into a list to get ride of quotations
                ESSID = ESSID[1] # get index 1 of ESSID list (0 = "ESSID: ", 1 = "Network Name")
                loNetwork = "lo: " + inet + " | ESSID: " + ESSID # store network inet and ESSID in a string
                print(loNetwork) # print lo network string
                lo = loNetwork # store lo network string as global lo variable
                networkTxt.write(inet) # write inet of connected network to network.txt
            else: # iwgetid string is empty
                loNetwork = "lo: " + inet # store network inet in a string
                print(loNetwork) # print lo network string
                lo = loNetwork # store lo network string as global lo variable

    IPtxt.write(wlan0 + "\n")
    IPtxt.write(eth0 + "\n")
    IPtxt.write(lo + "\n")

    #cmd= "ping " + wlan0
    #os.system (cmd)

main()
