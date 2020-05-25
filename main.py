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


interface = pyip.inputStr(prompt='What interface would you like to change?\n')
new_address = pyip.inputCustom(is_mac, prompt='Enter your new MAC Address:\n', limit=4,)

print('Changing MAC address of ' + interface + ' to ' + new_address)

subprocess.run('sudo ifconfig' + interface + 'down', shell=True)  # disconnect interface
subprocess.run(('sudo ifconfig' + interface + 'hw ether ' + new_address), shell=True) # Change the MAC
subprocess.run('sudo ifconfig' + interface + 'up', shell=True)  # Reconnect' + interface
subprocess.run('sudo ifconfig' + interface, shell=True)  # Return connection properties
