import csv

with open('ProgressSummary.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		string = str(row)
		if 'Calories' in string:
			calories = (''.join(filter(str.isdigit, string)))
			carbohydrates = (round((int(calories) * .6), 2))
			protein = (round((int(calories) * .1),2))
			fats = (round((int(calories) * .3),2))

			carbohydrates_calories = str(carbohydrates)
			protein_calories = str(protein)
			fats_calories = str(fats)

			carbohydrates_grams = str(round((carbohydrates/4), 2))
			protein_grams = str(round((protein/4), 2))
			fats_grams =str(round((fats/9), 2))

			print('Average daily calories burnt for the last seven days is '+ calories)
			print('Recommended daily carbohydrates intake equals ' + carbohydrates_calories + ' calories or ' + carbohydrates_grams + ' grams')
			print('Recommended daily protein intake equals ' + protein_calories + ' calories or ' + protein_grams + ' grams')
			print('Recommended daily fats intake equals ' + fats_calories + ' calories or ' + fats_grams + ' grams')