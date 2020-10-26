#!/usr/bin/env python
"""
Program that changes the MAC address of a system using user input.
"""

import subprocess


interface = raw_input("Interface > ")
new_mac = raw_input("New MAC > ")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] The MAC address of " + interface + " has been changed to " + new_mac)
