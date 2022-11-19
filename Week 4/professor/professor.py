import random

def get_level():
	try:
		while True:
			levels = [1, 2, 3]
			n = int(input("Level: "))
			if n in levels:
				return n
	except ValueError:
		n = int(input("Level: "))

def generate_integer(n):
	if n == 1:
		x = random.randint(0, 9)
		y = random.randint(0, 9)
	elif n == 2:
		x = random.randint(10, 99)
		y = random.randint(10, 99)
	elif n == 3:
		x = random.randint(100, 999)
		y = random.randint(100, 999)
	return x, y

def main():
	n = get_level()
	points = 0
	for i in range(10):
		num_conta = generate_integer(n)
		conta = "{} + {} = " .format(num_conta[0], num_conta[1])
		resp_correct = num_conta[0] + num_conta[1]

		for j in range(3):
			resp_user = int(input(conta))

			if resp_user == resp_correct:
				points += 1
				break
			else:
				print("EEE")
				if j == 2:
					print(conta, resp_correct)

	print(points)

if __name__ == "__main__":
    main()