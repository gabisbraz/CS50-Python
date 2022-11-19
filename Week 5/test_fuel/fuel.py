def main():
	getFraction = input("Fraction 1: ")
	percentage = gauge(convert(getFraction))
	print(percentage)

def convert(getFraction):
	try:
		nums = getFraction.split('/')
		x = int(nums[0])
		y = int(nums[1])
		div = x / y
	except(ZeroDivisionError, ValueError):
		raise
	else:
		div = round(div * 100)
		return div

def gauge(div):
	if div >= 0 and div <= 100:
		if (div >= 99):
			return "F"
		elif (div <= 1):
			return "E"
		elif (div <= 99 and div >= 1):
			percent = "{}%" .format(div)
			return percent

if __name__ == "__main__":
    main()
