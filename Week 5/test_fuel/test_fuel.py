from fuel import convert, gauge
import pytest

def test_convert():
	assert convert("2/5") == (40)
	assert convert("3/4") == (75)
	assert convert("1/4") == (25)
	assert convert("4/4") == (100)
	assert convert("0/4") == (0)
	with pytest.raises(ValueError):
		convert("gabi/braz")
	with pytest.raises(ZeroDivisionError):
		convert("7/0")

def test_gauge():
	assert gauge(40) == "40%"
	assert gauge(75) == "75%"
	assert gauge(25) == "25%"
	assert gauge(100) == "F"
	assert gauge(99) == "F"
	assert gauge(0) == "E"
	assert gauge(1) == "E"


def main():
	convert()
	gauge()

if __name__ == "__main__":
	main()