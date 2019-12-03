# Sean Cosgrove and Emery Wollerscheid
# Green Mountain Pi
# CS 121 Final Project
# repoToWeb.py

import os

def main():

    # copy contents of gmpi folder to web server
    gmpiCmd = "sudo cp -r ../gmpi/* ~/../../var/www/html"
    os.system(gmpiCmd)

    # copy contents of network folder to web server
    networkCmd = "sudo cp -r ../network/* ~/../../var/www/network"
    os.system(networkCmd)

    # copy contents of firewall folder to web server
    firewallCmd = "sudo cp -r ../firewall/* ~/../../var/www/firewall"
    os.system(firewallCmd)

    # copy contents of anti folder to web server
    antiCmd = "sudo cp -r ../anti/* ~/../../var/www/anti"
    os.system(antiCmd)

    # copy contents of tools folder to web server
    toolsCmd = "sudo cp -r ../tools/* ~/../../var/www/tools"
    os.system(toolsCmd)

main()
