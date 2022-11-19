def entrada():
	entrada = input("Data: (M/D/A) ")
	entrada = entrada.title()
	return entrada


def main():
	meses_extenso = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	meses_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

	data = entrada()
	virgula = ','
	barra = '/'
	while True:
		try:
			for item in data:
				alpha_num = item.isnumeric()

				if alpha_num == True:
					lista_entrada_numeros = data.split('/')
					mes = lista_entrada_numeros[0]
					dia = lista_entrada_numeros[1]
					ano = lista_entrada_numeros[2]
					if int(dia) > 31:
						data = entrada()
					if int(mes) > 12:
						data = entrada()
					else:
						if int(mes) in meses_numeros:
							dia_completo = dia.zfill(2)
							mes_completo = mes.zfill(2)
							break

				elif alpha_num == False:
					if virgula in data:
						lista_entrada_extenso = data.split(" ")
						dia = lista_entrada_extenso[1].strip(",")
						dia_completo = dia.zfill(2)
						mes = lista_entrada_extenso[0]
						ano = lista_entrada_extenso[2]
						if int(dia) > 31:
							data = entrada()
						if mes == mes.isalpha():
							data = entrada()
						tamanho = len(meses_extenso)
						for i in range(tamanho):
							if mes == meses_extenso[i]:
								mes = str(meses_numeros[i])
								mes_completo = mes.zfill(2)
								break
						break

		except(IndexError, ValueError):
			data = input("Data: (M/D/A) ")
		else:
			print("{}-{}-{}".format(ano, mes_completo, dia_completo))
			break


main()
