def outputAsCSV(filename, contents):
	fp = open(filename, 'w')
	for line in contents:
		fp.write(line + '\n')
	fp.close()