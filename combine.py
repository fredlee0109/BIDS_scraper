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

def isSocial(link):
	if link.find("facebook") != -1 and link.find("media") != -1:
		return True
	if link.find("linkedin") != -1 or link.find("angel.co") != -1 or link.find("twitter") != -1:
		return True
	return False

cdata = {}
with open('cleaned.csv', 'rb') as cleaned:
	reader = csv.reader(cleaned, delimiter=',')
	first = True
	for row in reader:
		if first:
			first = False
		else:
			cdata[row[0]] = row[4]
with open('full.csv', 'rb') as full:
	reader = csv.reader(cleaned, delimiter=',')
	first = True
	for row in reader:
		if first:
			first = False
		else:
			if row[0] in cdata and len(cdata[row[0]]) != 0:
				for link in cdata[row[0]]:
					if isSocia(link):
						


with open('cleaned.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Startup', "Institution", "Funds", "Alive?", "URLs", "Competitions", "Founders"])
	for company in data:
		writer.writerow([company] + [data[company][0]] + [locale.currency(data[company][1], grouping=True)] \
			+ [data[company][2]]+ [data[company][3]] + [data[company][4]])