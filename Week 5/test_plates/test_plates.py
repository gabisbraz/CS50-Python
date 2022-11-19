from plates import is_valid

def test_isValid():
	assert is_valid("CS50") == True
	assert is_valid("CS05") == False
	assert is_valid("PI3.14") == False
	assert is_valid("H") == False
	assert is_valid("OUTATIME") == False
	assert is_valid("15gabi") == False
	assert is_valid("Ga15BI") == False
	assert is_valid("GABI15") == True
	assert is_valid("1G") == False
	assert is_valid("15") == False
	assert is_valid("G4") == False

def main():
	is_valid()

if __name__ == "__main__":
	main()