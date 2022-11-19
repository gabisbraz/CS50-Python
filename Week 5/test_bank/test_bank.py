from bank import value

def test_value():
	assert value("hello") == 0
	assert value("HELLO") == 0
	assert value("Hello") == 0
	assert value("Hey") == 20
	assert value("hi") == 20
	assert value("How you doing?") == 20
	assert value("What's happening?") == 100

def main():
	value()

if __name__ == "__main__":
	main()