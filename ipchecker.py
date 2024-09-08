import argparse
import requests

parser = argparse.ArgumentParser(
    prog='ipchecker', 
    usage="python ipchecker.py IPADDR", 
    description="Check if IP address is malicious or not", 
    conflict_handler='error', 
    add_help=True
)

parser.add_argument("IPADDR",  help="The IP address you want to scan with Virus Total")
args = parser.parse_args()


print(args.IPADDR)

def scan_ip(IP):
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + IP
    return url    

targetIP = scan_ip(args.IPADDR)

headers = {
    "accept" : "application/json",
    "x-apikey" : "<APIKEY>"
}

response = requests.get(targetIP, headers=headers)

print(response.text)

