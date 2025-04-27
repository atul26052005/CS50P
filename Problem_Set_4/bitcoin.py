import requests
import sys

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate_str = response.json()["bpi"]["USD"]["rate"]
    rate = float(rate_str.replace(",", ""))
    
    amount = number_of_bitcoins * rate
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("Failed to fetch Bitcoin price")
    sys.exit(1)