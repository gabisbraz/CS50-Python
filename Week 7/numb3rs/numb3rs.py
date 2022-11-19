import re
#python numb3rs.py

def main():
  print(validate(input("IPv4 Address: ")))

def validate(ip):
	ip = ip.strip()
	try:
		if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
			inv = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
			for i in range(1, 5):
				x = int(inv.group(i))
				if x >= 0 and x <= 255:
					continue
				else:
					return False
			return True
		else:
			return False
	except(ValueError):
		return False

if __name__ == "__main__":
    main()