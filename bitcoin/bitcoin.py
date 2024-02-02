import requests
from sys import argv, exit;

try:
    number = float(argv[1]);

except ValueError:
    exit("Command-line argument is not a number");

except IndexError:
    exit("Missing command-line argument");

if number <= 0:
    exit("Command-line argument must be greater than 0");


try:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url);

except requests.RequestException:
    exit("API error");

try:
    data = response.json()
    data =  data['bpi']["USD"]

except (KeyError, TypeError, ValueError):
    exit("API error");


print(f"${number * data['rate_float']:,.4f}");