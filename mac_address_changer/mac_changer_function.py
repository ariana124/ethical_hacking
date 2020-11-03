#!/usr/bin/env python
"""
Program that changes the MAC address of a system using user input.
"""

import subprocess
import optparse


def arg_parser():
    # Creates an instance of the OptionParse class that's used to handle user input.
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    if not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info")
    return options

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] The MAC address of " + interface + " has been changed to " + new_mac)


# Parses the arguments on the command line and stores the arguments into the arguments variable and the value of it into the options variable.
(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)
