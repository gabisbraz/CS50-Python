x = str(input("Greeting: "))
hello = "Hello"

if hello in x:
    print("$0")
elif (x[0] == 'H' or x[0] == 'h'):
    print("$20")
else:
    print("$100")
		