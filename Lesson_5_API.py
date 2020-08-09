import urllib.request, json

# Opening a web request
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=fc4e8afdcb3e8ea6dadc")

# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
results = data['USD_PHP']
# USD_ILS = results['USD_ILS']
# val = USD_ILS['val']
print(results)
print(results)
print(results)