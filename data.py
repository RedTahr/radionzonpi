#import json,urllib
#data = urllib.urlopen("https://api.github.com/users?since=100").read()
#output = json.loads(data)
#print (output)

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

# url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=...."
url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"

response = urlopen(url)
data = response.read().decode("utf-8")
jdata = json.load(response)
jsondata = json.load(data)

print (data)