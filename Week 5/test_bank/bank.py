def value(x):
	if "hello" in x.lower():
			return 0
	elif (x[0] == 'H' or x[0] == 'h'):
			return 20
	else:
			 return 100

def main():
	x = input("Greeting: ")
	result = value(x)
	print("${}".format(result))

if __name__ == "__main__":
    main()