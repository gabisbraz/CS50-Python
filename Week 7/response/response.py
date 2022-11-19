from validator_collection import validators, checkers, errors

def main():
	print(email(input("What's your email address? ")))

def email(name):
	try:
		email_address = validators.email(name)
	except (errors.EmptyValueError, errors.InvalidEmailError):
		return "Invalid"
	else:
		return "Valid"

if __name__ == "__main__":
	main()