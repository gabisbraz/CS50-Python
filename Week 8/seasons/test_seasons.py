from seasons import minutos
import pytest

def test_minutos():
	assert minutos("1999-01-01") == "Twelve million, five hundred forty-five thousand, two hundred eighty minutes"
	assert minutos("1999-12-31") == "Twelve million, twenty-one thousand, one hundred twenty minutes"
	with pytest.raises(SystemExit):
		minutos("January 1, 1999")
	with pytest.raises(SystemExit):
		minutos("1999/12/31")

def main():
	minutos()

if __name__ == "__main__":
	main()