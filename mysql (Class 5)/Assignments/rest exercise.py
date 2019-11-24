import urllib.request, json
with urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=n&apiKey=bfe112e54d45be9759d8") as url:
    data = json.loads(url.read().decode())
results = data['results']
ILS_USD = results['ILS_USD']
currency_value = ILS_USD['val']
print("Welcome to currency converter")
try:
    amount = float(input("Please enter an amount of Shekeles to convert:"))
    print("The total amount after conversion is:", float(amount * currency_value))
    print("Thanks for using our currency converter")
except ValueError:
    print("Invalid Choice")