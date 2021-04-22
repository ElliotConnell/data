#run printer


import csv

date = input("input date: ")

with open ('Activities.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		string = str(row)
		if 'Date' in string:
			print(row)

		if date in string:
			print(row)

