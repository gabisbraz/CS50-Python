import sys

def main():
	try:
		nome_documento = sys.argv[1]

		if len(sys.argv) < 2:
			sys.exit("Too many command-line arguments")
		if len(sys.argv) > 2:
			sys.exit("Too many command-line arguments")
		if nome_documento.endswith(".py") == False:
			sys.exit("Not a Python file")

		if len(sys.argv) == 2 and nome_documento.endswith(".py"):
			print(arquivo(nome_documento))

	except(FileNotFoundError):
		sys.exit("File does not exist")

def arquivo(nome_arquivo):
	num_linhas = 0
	file = open(nome_arquivo, "r", encoding="utf-8")
	for linha in file:
		if linha_valida(linha) == True:
			num_linhas += 1
	return num_linhas

def linha_valida(linha):
	if linha.isspace():
		return False
	if linha.lstrip().startswith("#"):
		return False
	return True

main()