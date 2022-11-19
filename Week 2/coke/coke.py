valorCoca = 50
print("Amount Due:", valorCoca)

entrada = int(input("Insert coin: "))

while (entrada != 25 and entrada != 10 and entrada != 5):
	print("Amount Due:", valorCoca)
	entrada = int(input("Insert coin: "))

troco = valorCoca - entrada
print("Amount Due:", troco)

while troco != 0:
	entrada = int(input("Insert coin: "))
	if (entrada == 25 or entrada == 10 or entrada == 5):
		troco2 = troco - entrada
		troco = troco2 + 0
		if (troco == 0):
			print("Change Owed:", troco)
			break
		elif (troco < 0):
			print("Amount Due:", -troco)
			break
	print("Amount Due:", troco)

#50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
