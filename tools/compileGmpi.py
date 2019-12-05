# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# compileGmpi.py

import os
import time

def main():

    cmdCooldown = 3
    printCooldown = 1

    # execute updateNetwork.py
    updateNetwork = "../network/updateNetwork.py"
    networkCmd = "sudo python3 " + updateNetwork
    print("Updating network data...")
    time.sleep(printCooldown)
    os.system(networkCmd)
    time.sleep(cmdCooldown)
    print("Network updated")
    time.sleep(printCooldown)

    # copy contents of firewall folder to web server
    updateFirewall = "../firewall/updateFirewall.py"
    firewallCmd = "sudo python3 " + updateFirewall
    print("Updating firewall data...")
    time.sleep(printCooldown)
    os.system(firewallCmd)
    time.sleep(cmdCooldown)
    print("Firewall updated")
    time.sleep(printCooldown)

    print("Would you like to run an antimalware scan? (y/n)")
    response = str(input())
    if (str.lower(response) == "y"):
        print("|==============================|")
        antiScanCmd = "sudo rkhunter --check"
        os.system(antiScanCmd)
        time.sleep(cmdCooldown)
        print("Rootkit hunter scan complete")
        print("|==============================|")
        time.sleep(printCooldown)
    else:
        print("Loading most recent scan...")
        time.sleep(printCooldown)
    updateAntimalware = "../anti/updateAntimalware.py"
    antiCmd = "sudo python3 " + updateAntimalware
    print("Updating antimalware data...")
    time.sleep(printCooldown)
    os.system(antiCmd)
    time.sleep(cmdCooldown)
    print("Antimalware updated")
    time.sleep(printCooldown)
    print("|===== GMPI BUILD SUCCESS =====|") # build success

main()

