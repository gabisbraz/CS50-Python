from numb3rs import validate

def test_validate_true():
	assert validate("127.0.0.1") == True
	assert validate("255.255.255.255") == True

def test_validate_false():
	assert validate("512.512.512.512") == False
	assert validate("14.25.512.76") == False
	assert validate("1.2.3.1000") == False
	assert validate("1,2,3.1000") == False
	assert validate("cat") == False
	assert validate("125") == False

def main():
	validate()

if __name__ == "__main__":
	main()