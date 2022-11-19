#python bitcoin.py
import sys
import requests

try:
	n = float(sys.argv[1])
	#if sys.argv[1].isnumeric == True:
		#print("uh")
except (requests.RequestException, ValueError):
	print("Command-line argument is not a number")


#print(f"${amount:,.4f}")