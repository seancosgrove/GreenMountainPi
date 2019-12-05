# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# compileGmpi.py

import os
import time

def main():

    # initialize cooldown variables
    cmdCooldown = 3 # cooldown in between os command
    printCooldown = 1 # cooldown in between print statements

    # get connect inet address
    networkTxt = open("../network/network.txt", "r") # open network.txt file with connected network inet
    inet = networkTxt.read() # read file into string

    # execute updateNetwork.py
    updateNetwork = "../network/updateNetwork.py" # get path to updateNetwork.py
    networkCmd = "python3 " + updateNetwork # prepare os command
    print("Updating network data...") # print to terminal
    time.sleep(printCooldown) # print cooldown
    os.system(networkCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown
    print("Network updated") # print to terminal
    time.sleep(printCooldown) # print cooldown

    # execute updateFirewall.py
    updateFirewall = "../firewall/updateFirewall.py" # get path to updateFirewall.py
    firewallCmd = "python3 " + updateFirewall # prepare os command
    print("Updating firewall data...") # print to terminal
    time.sleep(printCooldown) # print cooldown
    os.system(firewallCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown
    print("Firewall updated") # print to terminal
    time.sleep(printCooldown) # print cooldown

    # execute updateAntimalware.py
    updateAntimalware = "../anti/updateAntimalware.py" # get path to updateAntimalware.py
    antiCmd = "python3 " + updateAntimalware # prepare os command
    print("Updating antimalware data...") # print to terminal
    time.sleep(printCooldown) # print cooldown
    os.system(antiCmd) # run os command
    time.sleep(cmdCooldown) # command cooldown
    print("Antimalware updated") # print to terminal
    time.sleep(printCooldown) # print cooldown

    # build success message
    print("|===== GMPI BUILD SUCCESS =====|")
    print("| Visit the Green Mountain Pi  |")
    print("| website at: " + inet + "     |")
    print("|==============================|")

main()

