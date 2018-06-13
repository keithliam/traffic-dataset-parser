from TrafficDataParser import TrafficDataParser

def printRoadChoices():
	print()
	print('[1] EDSA')
	print('[2] Commonwealth')
	print('[3] Quezon Avenue')
	print('[4] España')
	print('[5] C5')
	print('[6] Ortigas')
	print('[7] Marcos Highway')
	print('[8] Roxas Blvd.')
	print('[9] SLEX')

def printDirectionChoices():
	print()
	print('[1] Northbound')
	print('[2] Southbound')

def getRoadName(road):
	if road == 1:
		return 'edsa'
	elif road == 2:
		return 'commonwealth'
	elif road == 3:
		return 'quezon_avenue'
	elif road == 4:
		return 'españa'
	elif road == 5:
		return 'c5'
	elif road == 6:
		return 'ortigas'
	elif road == 7:
		return 'marcos_mighway'
	elif road == 8:
		return 'oxas_blvd.'
	else:
		return 'slex'

def getRoad():
	road = 0
	while road < 1 or 9 < road:
		printRoadChoices()
		road = int(input('Choose road: '))
	return getRoadName(road)

def getDirectionName(direction):
	if direction == 1:
		return 'northbound'
	else:
		return 'southbound'

def getDirection():
	direction = 0
	while direction < 1 or 2 < direction:
		printDirectionChoices()
		direction = int(input('Choose direction: '))
	return getDirectionName(direction)

parser = TrafficDataParser(getRoad(), getDirection(), 'data/')
parser.parse()