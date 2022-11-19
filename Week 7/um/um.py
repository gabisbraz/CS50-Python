import re

def main():
	print(count(input("Text: ")))

def count(s):
	s = s.strip()
	if re.search(r"(?i)(.+\s)?(\bum\b).?\s?(.+)?", s):
		x = re.findall(r"(?i)(\bum\b)", s)
		qtd_um = len(x)
		return qtd_um
	else:
		return 0

if __name__ == "__main__":
	main()