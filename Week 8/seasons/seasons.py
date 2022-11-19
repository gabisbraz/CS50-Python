from datetime import date
import re, sys, inflect

def minutos(data):
	data = data.strip()
	if re.search(r"\d+-\d+-\d+", data):
		hoje = date.today()
		hoje = date(hoje.year, hoje.month, hoje.day)
		data = data.split("-")
		passado = date(int(data[0]), int(data[1]), int(data[2]))
		tempo_decorrido = abs(hoje - passado)
		dias_decorridos = tempo_decorrido.days
		minutos_decorridos = dias_decorridos * 24 * 60
		p = inflect.engine()
		minutos_escritos = p.number_to_words(minutos_decorridos, andword="") + " minutes"
		return minutos_escritos.capitalize()
	else:
		sys.exit("Invalid date")

def main():
	print(minutos(input("Date of Birth: ")))

if __name__ == "__main__":
    main()