import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
	s = s.strip()
	if "youtube" in s and "iframe" in s:
		l = re.sub(r'.+src="\w+://w*?\.?youtube.com/embed/', "https://youtu.be/", s)
		#print(l)
		l2 = l.split('"')
		#print(l2)
		for i in range(len(l2)):
			if "youtu.be" in l2[i]:
				return l2[i]
	else:
		return None

if __name__ == "__main__":
    main()