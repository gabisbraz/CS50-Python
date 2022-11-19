entrada = input("Frase desejada para conversão: ")
print("Saída: ", end="")

for letras in entrada:
	if (letras == 'a' or letras == 'A'):
		print(end="")

	elif (letras == 'e' or letras == 'E'):
		print(end="")

	elif (letras == 'i' or letras == 'I'):
		print(end="")

	elif (letras == 'o' or letras == 'O'):
		print(end="")

	elif (letras == 'u' or letras == 'U'):
		print(end="")

	else:
		print(letras, end="")

print("\n")