#!/usr/bin/env python
"""
Program that changes the MAC address of a system using user input.
"""

import subprocess
import optparse

# Creates an instance of the OptionParse class.
parser = optparse.OptionParse()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")

# Parses the arguments on the command line.
parser.parse_args()

interface = raw_input("Interface > ")
new_mac = raw_input("New MAC > ")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] The MAC address of " + interface + " has been changed to " + new_mac)
