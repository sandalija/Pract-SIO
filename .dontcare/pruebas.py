import csv

def cleanCSV(datafile):
	f = open(datafile, 'r')
	data = csv.reader(f, delimiter =';')
	w = open('cleanCSV.csv', 'w')
	specials = '99'
	specials2 = '\''
	result = []

	for line in data:
		line = [value.replace(specials, '') for value in line]
		line = [value.replace('[', '') for value in line]
		line = [value.replace(']', '') for value in line]
		line = [value.replace('\'', '') for value in line]
		w.write("%s\n" % line)
		result.append(line)
	f.close()
	return result

cleanCSV('dataset.csv')