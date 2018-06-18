def outputAsCSV(filename, contents):
	fp = open(filename, 'w')
	fp.write(contents)
	fp.close()