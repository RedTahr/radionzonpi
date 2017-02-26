import json
from urllib.request import urlopen
url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
response = urlopen(url)
print (response)
data = response.read().decode("utf-8")
print(data)