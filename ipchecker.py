import sys
import requests

headers = {
    "accept" : "application/json",
    "x-apikey" : "<APIKEY>"
}


IPLIST = ['10.10.10.10','22.2.2.2']
text = input("Enter IP address: ")
print(text)

def make_urls():
    URLS = []
    for ip in IPLIST:
        url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip
        URLS.append(url)
    return URLS    

URLLIST = make_urls()
print(URLLIST)