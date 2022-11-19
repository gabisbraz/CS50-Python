def entrada():
	entrada = input("Item: ")
	item = str.title(entrada)
	return item

def main():
	produto_preco = {
						"Baja Taco": 4.00,
						"Burrito": 7.50,
						"Bowl": 8.50,
						"Nachos": 11.00,
						"Quesadilla": 8.50,
						"Super Burrito": 8.50,
						"Super Quesadilla": 9.50,
						"Taco": 3.00,
						"Tortilla Salad": 8.00
					}

	preco_total = 0
	while True:
		try:
			item = entrada()
		except (EOFError, KeyError):
			print("\n")
			break
		else:
			if item in produto_preco:
				preco_individual = produto_preco[item]
				preco_total = preco_total + preco_individual
				print("Total: ${0:.2f} " .format(preco_total))

main()