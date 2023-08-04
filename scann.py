# import pyfiglet module
import pyfiglet
import scapy.all as scapy
import re

result = pyfiglet.figlet_format("Alan_Jolly")
print(result)

ip_add = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ip_add_given = input("\nenter the ip address range")
    if ip_add.search(ip_add_given):
        print(f"{ip_add_given} is a valid ip address")
        break

arp_result = scapy.arping(ip_add_given)


