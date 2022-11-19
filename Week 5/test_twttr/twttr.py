def shorten(palavra):
	alfa_minusc = ["a", "e", "i", "o", "u"]
	alfa_maiusc = ["A", "E", "I", "O", "U"]
	x = ""
	for letras in palavra:
			if letras not in alfa_maiusc and letras not in alfa_minusc:
					x = x + letras
			elif letras in alfa_maiusc or letras in alfa_minusc:
					x = x + ""
	return x

def main():
	palavra = input("Frase desejada para conversão: ")
	print("Saída: ", end="")
	result = shorten(palavra)
	print(result, end="\n")

if __name__ == "__main__":
    main()