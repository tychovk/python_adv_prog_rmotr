import requests
from pprint import pprint as pp
resp = requests.get('http://httpbin.org/get')
if resp.ok:
    print("Request successful. Here's the data")
    pp(resp.json())
    

# if resp.ok == false, still you can have a connection


resp2 = requests.get('http://httpbin.org/')

if resp2.ok:
    print("second is also ok.")
    pp(resp2.json())