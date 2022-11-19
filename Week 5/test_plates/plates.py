def main():
	placa = input("Placa escolhida: ")
	result = is_valid(placa)
	if result == False:
		print("Invalid")
	else:
		print("Valid")


def is_valid(placa):
	lista = []
	lista_num = []
	for letra in placa:
		lista.append(letra)

	if len(lista) <= 6 and len(lista) >= 2:
		True
	else:
		return False

	if lista[0].isalpha() and lista[1].isalpha():
		True
	else:
		return False

	for caractere in lista:
		if caractere.isalpha() or caractere.isdigit():
			True
		else:
			return False

	for caractere in lista:
		if caractere.isdigit():
			lista_num.append(caractere)
			if lista_num[0] == "0":
				return False
			else:
				True

	ultimo_num = len(lista_num)-1
	ultimo_caractere = len(lista)-1
	if len(lista_num) != 0:
		if lista_num[ultimo_num] == lista[ultimo_caractere] and lista[ultimo_caractere-1].isdigit():
			True
		else:
			return False

	return True

if __name__ == "__main__":
    main()