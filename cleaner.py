import csv

def clean(dollar):
	dollar  = dollar.replace("$", "").replace(",", "")
	if dollar.find(".") != -1:
		dollar = dollar[0:dollar.find(".")]
	return int(dollar)

with open('URAP.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	cols = []
	first = True
	data = {} # company name : ["Institution", "Funds", "Alive?", "URL"]
	for row in reader:
		# row: [competition, year, startup, fund, source of fund, ...]
		if first:
			first = False
		else:
			# print row[0] == ""
			if row[2] != "":
				if row[2] in data:
					if row[3] != "":
						data[row[2]][1] += clean(row[3])
					if row[5] != "":
						data[row[2]][3].append(row[5])
				else:
					if row[5] != "" and row[3] != "":
						data[row[2]] = ["", clean(row[3]), "", [row[5]]]
					elif row[5] != "":
						data[row[2]] = ["", 0, "", [""]]
					elif row[3] != "":
						data[row[2]] = ["", clean(row[3]), "", [""]]
					else:
						data[row[2]] = ["", 0, "", [""]]
with open('cleaned.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Startup', "Institution", "Funds", "Alive?", "URLs"])
	for company in data:
		writer.writerow([company] + [data[company][0]] + [data[company][1]] + [data[company][2]]+ [data[company][3]])