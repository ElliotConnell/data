
import csv

with open('test1.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['x', 'x', 'x', 'x', 'x'])
	writer.writerow(['y', 'y', 'y', 'y', 'y'])
