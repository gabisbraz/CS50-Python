chosenFruit = str.lower(input("Item: "))

listFruits = ['apple', 'avocado', 'banana', 'cantaloupe', 'grapefruit', 'grapes', 'honeydew', 'kiwifruit',
'lemon', 'lime', 'nectarine', 'orange', 'peach', 'pear', 'pineapple', 'plums', 'strawberries', 'sweet cherries',
 'tangerine', 'watermelon']

caloriesFruits = [130, 50, 110, 50, 60, 90, 50, 90, 15, 20, 60, 80, 60, 100, 50, 70, 50, 100, 50, 80]

cont = 0

for fruit in listFruits:
	calories = caloriesFruits[cont]
	if (fruit == chosenFruit):
		print("Calories:", calories)
	cont += 1
	##print(cont, "-", fruit, "-", calories)
