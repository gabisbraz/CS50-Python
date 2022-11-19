from jar import Jar
import pytest

def test_init():
	jar = Jar()
	assert jar.capacity == 12
	with pytest.raises(ValueError):
		Jar(-3)

def test_str():
	jar = Jar()
	jar.deposit(5)
	assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
	jar = Jar()
	jar.deposit(5)
	assert jar.size == 5
	jar.deposit(5)
	assert jar.size == 10

def test_withdraw():
	jar = Jar()
	jar.deposit(8)
	jar.withdraw(3)
	assert jar.size == 5


def main():
	Jar()

if __name__ == "__main__":
	main()