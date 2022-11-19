entrada = input("Frase desejada para conversão: ")
print("Saída: ", end="")

for letras in entrada:
    if letras.isupper():
        print("_" + letras.lower(), end="")
    else:
        print(letras, end="")

print("\n")