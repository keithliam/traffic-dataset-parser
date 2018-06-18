def outputAsCSV(filename, contents):
	fp = open(filename)
	fp.write(contents)
	fp.close()