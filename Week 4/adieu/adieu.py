import inflect

juntar = inflect.engine()

lista_nomes = []

while True:
	try:
		nome = input("Name: ")
	except EOFError:
		print("\b")
		break
	else:
		lista_nomes.append(nome)

nomes_print = juntar.join(lista_nomes, final_sep="")
print("Adieu, adieu, to", nomes_print)
