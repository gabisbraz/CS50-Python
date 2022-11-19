import sys
from tabulate import tabulate

def main():
	try:
		nome_documento = sys.argv[1]

		if len(sys.argv) < 2:
			sys.exit("Too many command-line arguments")
		if len(sys.argv) > 2:
			sys.exit("Too many command-line arguments")
		if nome_documento.endswith(".csv") == False:
			sys.exit("Not a CSV file")

		if len(sys.argv) == 2 and nome_documento.endswith(".csv"):
			n_linhas = arquivo(nome_documento)
			tabela(n_linhas[1])

	except(FileNotFoundError):
		sys.exit("File does not exist")

def arquivo(nome_arquivo):
	num_linhas = 0
	M = []
	file = open(nome_arquivo, "r", encoding="utf-8")
	for linha in file:
		lista = []
		if linha_valida(linha) == True:
			num_linhas += 1
			linha = linha.rstrip("\n")
			lista = linha.split(",")
			M.append(lista)
	return num_linhas, M

def linha_valida(linha):
	if linha.isspace():
		return False
	if linha.lstrip().startswith("#"):
		return False
	return True

def tabela(matriz):
	headers = matriz[0]
	matriz.remove(matriz[0])
	print(tabulate(matriz, headers, tablefmt="grid"))


main()