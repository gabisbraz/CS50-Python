def entrada():
	entrada = input()
	item = str.upper(entrada)
	return item

def main():
	lista_produtos = {}
	while True:
		try:
			item = entrada()
		except (EOFError, KeyError):
			print("\n")
			break
		else:
			if item in lista_produtos:
				lista_produtos[item] += 1
			else:
				lista_produtos[item] = 1
	for item in sorted(lista_produtos.keys()):
		print(lista_produtos[item], item)

main()