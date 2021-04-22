

#import the csv module

import csv

with open('test.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in reader:
		print(', '.join(row))