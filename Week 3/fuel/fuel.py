while True:
	try:
		getFraction = input("Fraction 1: ")
		nums = getFraction.split('/')
		x = int(nums[0])
		y = int(nums[1])
		div = x / y
	except(ZeroDivisionError, ValueError):
		getFraction = input("Fraction 2: ")
		break
	else:
		if x > y:
			getFraction = input("Fraction 2: ")
			#percent = round(div * 10)
			#print(percent, end='% \n')
		elif (x == y or div >= 0.99):
			print("F")
		elif (x == 0 or div <= 0.01):
			print("E")
		elif x < y:
			percent = round(div * 100)
			print(percent, end='% \n')
		break


#print(f"{x:.1f}")
# prompt the user again, if:
# X or Y is not an integer
# X is greater than Y
# Y is 0
