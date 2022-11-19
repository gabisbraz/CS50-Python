def main():
		getFraction = input("Fraction 1: ")
		nums = getFraction.split('/')
		x = int(nums[0])
		y = int(nums[1])
		div = x / y
		return x, y

def get_int():
	while True:
		try:
			main()
		except(ZeroDivisionError, ValueError):
			main(x, y)
		else:
			if x > y:
				percent = int(div * 10)
				print(percent, end='% \n')
			elif (x == y or div >= 0.99):
				print("F")
			elif (x == 0 or div <= 0.01):
				print("E")
			elif x < y:
				percent = int(div * 100)
				print(percent, end='% \n')
			break

get_int()