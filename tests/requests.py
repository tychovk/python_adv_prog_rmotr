import requests
from ppint import pprint as pp
resp = requests.et('http://httpbin.org/get')
if resp.ok:
    print("Request successful. Here's data")
    pp(resp.json())