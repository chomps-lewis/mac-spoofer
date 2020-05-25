#!/usr/bin/env python

# Mac Address
# Media Access Control - Permanent Physical Unique
# Assigned by manufacturer
# No two devices in the world with the same MAC Address
# MAC address never changes
# Information flows from the source MAC to the destination MAC

# Changing/Spoofing the MAC address will
# Increase anonymity
# Impersonate other devices
# Bypass filters

# We're going to be using the subprocess Module
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False,
#                cwd=None, timeout=None, check=False,
#                encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)
# Subprocess contains functions that allow us to execute system commands
# Commands depend on the OS which executes the script


import subprocess, re
import pyinputplus as pyip


def is_mac(s):
    mac_regex = re.compile(r'(([A-F]|\d){2}:){5}([A-F]|\d){2}')
    mo1 = mac_regex.search(s)
    if mo1 is None:
        raise Exception('Not a valid MAC Address.')


response = pyip.inputCustom(is_mac, prompt='Enter your new MAC Address:\n', limit=4,)


subprocess.run('sudo ifconfig eth0 down', shell=True)  # disconnect eth0
subprocess.run(('sudo ifconfig eth0 hw ether ' + response), shell=True) # Change the MAC
subprocess.run('sudo ifconfig eth0 up', shell=True)  # Reconnect eth0
subprocess.run('sudo ifconfig eth0', shell=True)  # Return connection properties
