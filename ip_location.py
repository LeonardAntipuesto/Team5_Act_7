from urllib import response
import requests
from requests import get

ip = get('https://api64.ipify.org').text
# ip = get('https://ip6.seeip.org').text
print('Your IPV4 address is: {}'.format(ip))
# print('Your IPV6 address is: {}'.format(ip2))

response = requests.get("http://ip-api.com/json/"+ip).json()
print("\nCountry: "+response['country'])
print("Region Name: "+response['regionName'])
print("City: "+response['city'])
print("ZIP code: "+response['zip'])
lat = str(response['lat'])
print("Latitude: "+ lat)
lon = str(response['lon'])
print("Longitude: "+ lon)
print("ISP: "+response['isp'])
print("ASN: "+response['as'])
