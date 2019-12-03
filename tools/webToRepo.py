# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# webtoRepo.py

import os

def main():

    # copy contents of gmpi folder to web server
    gmpiCmd = "sudo cp -r ~/../../var/www/html/* ../gmpi"
    os.system(gmpiCmd)

    # copy contents of network folder to web server
    networkCmd = "sudo cp -r  ~/../../var/www/network/* ../network"
    os.system(networkCmd)

    # copy contents of firewall folder to web server
    firewallCmd = "sudo cp -r ~/../../var/www/firewall/* ../firewall"
    os.system(firewallCmd)

    # copy contents of anti folder to web server
    antiCmd = "sudo cp -r ~/../../var/www/anti/* ../anti"
    os.system(antiCmd)

    # copy contents of tools folder to web server
    toolsCmd = "sudo cp -r ~/../../var/www/tools/* ../tools"
    os.system(toolsCmd)


main()

