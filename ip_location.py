from urllib import response
import requests
from requests import get

ip = get('https://api64.ipify.org').text
# ip = get('https://ip6.seeip.org').text
print('Your IPV4 address is: {} \n'.format(ip))
# print('Your IPV6 address is: {}'.format(ip2))

response = requests.get("http://ip-api.com/json/"+ip).json()
x = response.items()
d = {'status':'Status:', 'country':'Country:', 'countryCode': 'Country Code:', 'region':'Region:','regionName':'Region Name:','city':'City:', 'zip':'ZIP Code:','lat':'Latitude:','lon':'Longitude:','timezone':'Timezone:','isp':'ISP:', 'org':'Org:', 'as':'ASN:', 'query':'Query:'}
change = dict((d[key], value) for (key, value) in x)
for z in change:
   print(z,change[z])

