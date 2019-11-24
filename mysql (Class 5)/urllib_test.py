# import urllib.request
# val = urllib.request.urlopen("https://www.google.com").read()
# print(val)
#
# # JSON
# import json
# x =  '{ "name":"John", "age":30, "city":"New York", "gender":"man"}'
# y = json.loads(x)
# print(y["gender"])

import urllib.request, json

# Opening a web request | Change compact = 'n'
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=bfe112e54d45be9759d8")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
results = data['results']
USD_ILS = results['USD_ILS']
val = USD_ILS['val']
print(val)