from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
lista = figlet.getFonts()

try:
	if sys.argv[1] == '-f' or sys.argv[1] == '--font':
		if sys.argv[2] not in lista:
			sys.exit("Invalid usage")
		texto = input("Texto: ")
		fonte = figlet.setFont(font=sys.argv[2])
		print(figlet.renderText(texto))
	else:
		sys.exit("Invalid usage")
except IndexError:
	texto = input("Texto: ")
	fonte = choice(lista)
	fonte_p = figlet.setFont(font=fonte)
	fonte_l = figlet.renderText(texto)
	print(fonte_l)

