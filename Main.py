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

def printEdsaPoints():
	print()
	print('[1] Balintawak')
	print('[2] Kaingin Road')
	print('[3] Muñoz')
	print('[4] Bansalangin')
	print('[5] North Avenue')
	print('[6] Trinoma')
	print('[7] Quezon Avenue')
	print('[8] NIA Road')
	print('[9] Timog')
	print('[10] Kamuning')
	print('[11] New York - Nepa Q-Mart')
	print('[12] Monte De Piedad')
	print('[13] Aurora Blvd')

def printCommonwealthPoints():
	print('[1] Batasan')
	print('[2] St. Peter\'s Church')
	print('[3] Ever Gotesco')
	print('[4] Diliman Preparatory School')
	print('[5] Zuzuarregi')
	print('[6] General Malvar Hospital')
	print('[7] Tandang Sora Eastside')
	print('[8] Tandang Sora Westside')
	print('[9] Central Avenue')
	print('[10] Magsaysay Avenue')
	print('[11] University Avenue')
	print('[12] Philcoa')

def getEdsaName(point):
	if point == 1:
		return 'Balintawak'
	elif point == 2:
		return 'Kaingin Road'
	elif point == 3:
		return 'Muoz'
	elif point == 4:
		return 'Bansalangin'
	elif point == 5:
		return 'North Ave.'
	elif point == 6:
		return 'Trinoma'
	elif point == 7:
		return 'Quezon Ave.'
	elif point == 8:
		return 'NIA Road'
	elif point == 9:
		return 'Timog'
	elif point == 10:
		return 'Kamuning'
	elif point == 11:
		return 'New York - Nepa Q-Mart'
	elif point == 12:
		return 'Monte De Piedad'
	else:
		return 'Aurora Blvd.'

def getEdsaPoint():
	road = 0
	while road < 1 or 13 < road:
		printEdsaPoints()
		road = int(input('Choose point: '))
	return getEdsaName(road)

def getRoadName(road):
	if road == 1:
		return 'EDSA ' + getEdsaPoint()
	elif road == 2:
		return 'COMMONWEALTH ' + getCommonwealthPoint()
	elif road == 3:
		return 'QUEZON AVE. ' + getQuezonAvePoint()
	elif road == 4:
		return 'ESPAA ' + getEspanaPoint()
	elif road == 5:
		return 'C5 ' + getC5Point()
	elif road == 6:
		return 'ORTIGAS ' + getOrtigasPoint()
	elif road == 7:
		return 'MARCOS HIGHWAY ' + getMarcosHwyPoint()
	elif road == 8:
		return 'ROXAS BLVD. ' + getRoxasBlvdPoint()
	else:
		return 'SLEX ' + getSlexPoint()

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