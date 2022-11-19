import random

def pegaGuess():
	g = int(input("Guess: "))
	return g

try:
	while True:
		n = input("Level: ")
		if int(n) > 0:
			g = pegaGuess()
			break

except (ValueError, TypeError):
	if n.isnumeric() == False or int(n) <= 0:
		n = input("Level: ")
	g = pegaGuess()

else:
	n = int(n)

	x = random.randint(1, n)

	while True:
		if g == x:
			print("Just right!")
			break
		elif g > x:
			print("Too large!")
		elif g < x:
			print("Too small!")
		g = pegaGuess()

	print(x)
