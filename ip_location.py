from urllib import response #import needed libraries
import requests
from requests import get
from flask import Flask, redirect, url_for, render_template

app = Flask('__main__')

@app.route("/")
def home():
   ip = get('https://ip.seeip.org').text # this is for getting IPV4 using seeip API

   #ipv6 = get('https://api64.ipify.org').text # this is for getting IPV6 using seeip API 
   # Uncomment the line if IPV6 is availabe

   print('Your IPV4 address is: {} \n'.format(ip)) # this displays the IPV4 address

   #print('Your IPV6 address is: {}'.format(ipv6)) # this displays the IPV6 address
   # Uncomment this line together with line 6 if IPV6 is available

   response = requests.get("http://ip-api.com/json/"+ip).json()
   # It gets the location of the provided api from the previous lines using the API ip-api

   x = response.items()
   # this sets the values from response to the variable x

   d = {'status':'Status', 'country':'Country', 'countryCode': 'Country Code', 'region':'Region','regionName':'Region Name','city':'City', 'zip':'ZIP Code','lat':'Latitude','lon':'Longitude','timezone':'Timezone','isp':'ISP', 'org':'Org', 'as':'ASN', 'query':'Query'}
   # sets different labels on the keys in dictionary 

   change = dict((d[key], value) for (key, value) in x)
   # changes the previous labels to the set label from variable d.

   return render_template("index.html",ip=ip,result=change)
   # prints the output to the html file

if __name__ == "__main__":
   app.run()