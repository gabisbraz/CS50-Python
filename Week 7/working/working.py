import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
	s = s.strip()
	if re.search(r"\d+:?\d*? \w+ to \d+:?\d*? \w+", s):
		horario = re.match(r"(.+) (\w+) to (.+) (\w+)", s)

		horario1 = horario.group(1).split(":")
		periodo1 = horario.group(2)

		horario2 = horario.group(3).split(":")
		periodo2 = horario.group(4)
		#print(horario1, horario2)

		if int(horario1[0]) > 12 or int(horario2[0]) > 12:
			raise ValueError

		if len(horario1) == 2:
			#Tem minutos
			min1 = int(horario1[1])
			min2 = int(horario2[1])
			if min1 >= 60 or min2 >= 60:
				raise ValueError
		else:
			#Não tem minutos
			min1 = 0
			min2 = 0


		if periodo1 == "AM" and periodo2 == "PM":
			if int(horario1[0]) == 12:
				horario1[0] = 0
			if int(horario2[0]) == 12:
				horario2 = 12
			else:
				horario2 = int(horario2[0]) + 12
			return "{:0>2}:{:0>2} to {:0>2}:{:0>2}" .format(horario1[0], min1, horario2, min2)

		if periodo1 == "PM" and periodo2 == "AM":
			if int(horario2[0]) == 12:
				horario2[0] = 0
			if int(horario1[0]) == 12:
				horario1 = 12
			else:
				horario1 = int(horario1[0]) + 12
			return "{:0>2}:{:0>2} to {:0>2}:{:0>2}" .format(horario1, min1, horario2[0], min2)

	else:
		raise ValueError

if __name__ == "__main__":
    main()