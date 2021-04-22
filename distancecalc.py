import csv


with open('ProgressSummary.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		string = str(row)
		if 'Distance' in string:
				summary_list = list(','.join(row))
				number = float(''.join((summary_list[15:])))
				proposed = str(round((number * 1.1), 0))
				previous = str(''.join((summary_list[15:])))

				print('You ran ' + previous + 'km last week')
				print('You need to run ' + proposed + 'km this week')
				print(summary_list)
		

#, quotechar='|'
#, delimiter=','

#(''.join(filter(str.isnumeric, string)))