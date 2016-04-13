import csv
import locale

locale.setlocale( locale.LC_ALL, '' ) # Set currency format for USD

def clean(dollar):
	if dollar.lower() == "undisclosed":
		return 0
	dollar  = dollar.replace("$", "").replace(",", "")
	if dollar.find("-") != -1:
		dollar = dollar.split("-")
		if dollar[0].find(".") != -1:
			dollar[0] = dollar[0][0:dollar[0].find(".")]
		if dollar[1].find(".") != -1:
			dollar[1] - dollar[1][0:dollar[1].find(".")]
		return (int(dollar[0]) + int(dollar[1])) / 2
	if dollar.find(".") != -1:
		dollar = dollar[0:dollar.find(".")]
	return int(dollar)

with open('URAP.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	cols = []
	first = True
	data = {} # company name : ["Institution", "Funds", "Alive?", "URL", "Competitions", "Founders"]
	prev = ""
	for row in reader:
		# row: [competition, year, startup, fund, source of fund, URL, ...]
		if first:
			first = False
		else:
			if row[2] != "":
				prev = row[2]
				if row[2] not in data:
					data[row[2]] = ["", 0, "", [], []]
				if row[3] != "":
					data[row[2]][1] += clean(row[3])
				if row[5] != "" and row[5] != "Awardee Reporting":
					data[row[2]][3].append(row[5])
				if row[0] != "":
					data[row[2]][4].append(row[0].replace("\n", " "))
			else:
				if row[3] != "":
					data[prev][1] += clean(row[3])
				if row[5] != "" and row[5] != "Awardee Reporting":
					data[prev][3].append(row[5])
				if row[0] != "" and row[0] not in data[prev][4]:
					data[prev][4].append(row[0].replace("\n", " "))

with open('cleaned.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Startup', "Institution", "Funds", "Alive?", "URLs", "Competitions", "Founders"])
	for company in data:
		writer.writerow([company] + [data[company][0]] + [locale.currency(data[company][1], grouping=True)] \
			+ [data[company][2]]+ [data[company][3]] + [data[company][4]])