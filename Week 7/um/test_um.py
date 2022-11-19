from um import count

def j():
	assert count('um') == 1
	assert count("um?") == 1
	assert count("Um, thanks for the album.") == 1
	assert count("Um, thanks, um...") == 2
	assert count("yum") == 0
	assert count("um um") == 2
	assert count("UM") == 1
	assert count("Um") == 1
	assert count("uM") == 1

def h():
	assert count("Um, thanks, um...") == 3
	assert count("um") == 0
	assert count("yummy") == 1
	assert count("yum") == 1

def main():
	count()

if __name__ == "__main__":
	main()