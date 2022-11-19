from twttr import shorten

def test_shorten():
	assert shorten("banana") == "bnn"
	assert shorten("BANANA") == "BNN"
	assert shorten("BanANa") == "BnN"
	assert shorten("1504") == "1504"
	assert shorten(".g?a'b,i!") == ".g?'b,!"

def main():
	shorten()

if __name__ == "__main__":
	main()