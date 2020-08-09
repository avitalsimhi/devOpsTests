import urllib.request, json
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=ultra&apiKey=fc4e8afdcb3e8ea6dadc")
data = json.loads(url.read().decode())
currency_value = data['ILS_USD']
print("Welcome to currency converter")
try:
    amount = float(input("Please enter an amount of Shekeles to convert: "))
    print("The result is: ", float(amount * currency_value))
    print("Thanks for using our currency converter")
except ValueError:
    print("Invalid Choice")