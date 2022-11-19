import emoji

x = input("Input: ")
lista = x.split(" ")
#emoji = []
for i in lista:
	for x in i:
		if x == ":":
			index = i
			#print(index)
			print(emoji.emojize('Output: {}' .format(index), language='alias'))
			#emoji.append(index)
			break

#print(emoji)
