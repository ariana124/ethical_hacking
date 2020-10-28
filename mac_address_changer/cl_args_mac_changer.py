#!/usr/bin/env python
"""
Program that changes the MAC address of a system using user input.
"""

import subprocess
import optparse

# Creates an instance of the OptionParse class that's used to handle user input.
parser = optparse.OptionParse()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

# Parses the arguments on the command line and stores the arguments into the options variable and the value of it into the argument variable.
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] The MAC address of " + interface + " has been changed to " + new_mac)
