# mac-spoofer
Spoof your MAC Address on Linux

Requires net-tools and ifconfig
Requires pyinputplus, subprocess, and re

The script will prompt you for input and will only accept a valid MAC Address formatted like:
A1:B2:C3:D4:E5:F6

Your mac address will then change to your input

Currently only works on eth0 interface, if yours is different this will not work. 

main.py will change your address -- Take note of what your original MAC Address was as it should be changed back after

# TODO
1) Allow spoofing of different connection interfaces
