import sys
import csv

def main():
	docs = doc_valido()
	doc_before = docs[0]
	doc_after = docs[1]
	matriz = arquivo(doc_before)
	#print(matriz)
	saida(matriz, doc_after)

def doc_valido():
	try:
		if len(sys.argv) < 3:
			sys.exit("Too few command-line arguments")
		doc_before = sys.argv[1]
		doc_after = sys.argv[2]
		if doc_before.endswith(".csv") == False and doc_after.endswith(".csv") == False:
			sys.exit("Not a CSV file")
		file = open(doc_before, "r", encoding="utf-8")
		if len(sys.argv) > 3:
			sys.exit("Too many command-line arguments")
		if len(sys.argv) == 3 and doc_before.endswith(".csv") and doc_after.endswith(".csv"):
			file = open(doc_after, "a", encoding="utf-8")
			return doc_before, doc_after
	except(FileNotFoundError):
		sys.exit("Could not read {}" .format(doc_before))

def arquivo(nome_documento):
	file = open(nome_documento, "r", encoding="utf-8")
	lista = []
	for line in file:
		line = line.rstrip("\n")
		linha = line.split(",")
		lista.append(linha)
	matriz = []
	for i in range(1, len(lista)-1):
		primeiro_nome = lista[i] [1].removeprefix(' ').removesuffix('"')
		segundo_nome = lista[i] [0].removeprefix('"')
		casa = lista[i] [2]
		linha_matriz = [primeiro_nome, segundo_nome, casa]
		matriz.append(linha_matriz)
	return matriz

def saida(matriz):
	saida = open("after.csv", "w", encoding="utf-8")
	saida.write("name, house")
	for linha in matriz:
		saida.write("\n{}, {}, {}" .format(linha[0], linha[1], linha[2]))


if __name__ == "__main__":
	main()