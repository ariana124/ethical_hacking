#!/usr/bin/env python
"""
Program that changes the MAC address of a system
"""

import subprocess


interface = "eth0"
new_mac = "00:11:33:55:77:99"


subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether" + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
