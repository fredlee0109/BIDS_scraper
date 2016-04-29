import csv
import locale
import numpy as np

locale.setlocale( locale.LC_ALL, '' ) # Set currency format for USD

def clean(comp):
	if comp[0] == ' ':
		comp = comp[1:]
	if comp[0] == ' ':
		comp = comp[1:]
	comp = filter(lambda x: x.isalpha() or x.isspace(), comp)
	if comp[-1] == " ":
		return comp[0:-1]
	return comp

def pretty(fund):
	return locale.currency(fund, grouping=True)

with open('data.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	first = True
	data = {} # Competition : [Funds]
	alive = {} # Competition : [Funds]
	dead = {} # Competition : [Funds]
	datas = 0
	alives = 0
	deads = 0
	for row in reader:
		# row: [competition, year, startup, fund, source of fund, URL, ...]
		if first:
			first = False
		else:
			if row[2][0] == '$':
				fund = int(row[2][1:-3].replace(",", ""))
				for comp in row[9].replace("\n", "").split(","):
					comp = clean(comp)
					if fund != 0:
						datas += 1
						if comp in data:
							data[comp].append(fund)
						else:
							data[comp] = [fund]
						if row[3] == "Yes":
							alives += 1
							if comp in alive:
								alive[comp].append(fund)
							else:
								alive[comp] = [fund]
						else:
							deads += 1
							if comp in dead:
								dead[comp].append(fund)
							else:
								dead[comp] = [fund]
print "For all companies, with", datas, "number of data:"
for comp in data:
	print "    For competition,", comp, "with", len(data[comp]), "number of data:"
	print "        average fund is", pretty(np.mean(data[comp]))
	print "        min fund is", pretty(min(data[comp]))
	print "        max fund is", pretty(max(data[comp]))
	print "        median fund is", pretty(np.median(data[comp]))
print ""
print "For alive companies, with", alives, "number of data:"
for comp in alive:
	print "    For competition,", comp, "with", len(alive[comp]), "number of data:"
	print "        average fund is", pretty(np.mean(alive[comp]))
	print "        min fund is", pretty(min(alive[comp]))
	print "        max fund is", pretty(max(alive[comp]))
	print "        median fund is", pretty(np.median(alive[comp]))
print ""
print "For dead or unkown companies, with", deads, "number of data:"
for comp in dead:
	print "    For competition,", comp, "with", len(dead[comp]), "number of data:"
	print "        average fund is", pretty(np.mean(dead[comp]))
	print "        min fund is", pretty(min(dead[comp]))
	print "        max fund is", pretty(max(dead[comp]))
	print "        median fund is", pretty(np.median(dead[comp]))