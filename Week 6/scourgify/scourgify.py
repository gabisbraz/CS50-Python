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

def arquivo(doc_before):
	matriz = []
	with open(doc_before, "r", encoding="utf-8") as file:
		line = csv.DictReader(file)
		for name_house in line:
			n = name_house["name"].split(",")
			first_name = n[1].lstrip()
			last_name = n[0]
			house = name_house["house"]
			matriz.append({"first": first_name, "last": last_name, "house": house })
	return matriz

def saida(matriz, doc_after):
	with open(doc_after, "w") as file:
		linha = csv.DictWriter(file, fieldnames=["first", "last", "house"])
		linha.writerow({"first": "first", "last": "last", "house": "house"})
		for coluna in matriz:
			first_name = coluna["first"]
			last_name = coluna["last"]
			house = coluna["house"]
			linha.writerow({"first": first_name, "last": last_name, "house": house})

if __name__ == "__main__":
	main()