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
	print()
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

def printQuezonAvePoints():
	print()
	print('[1] Elliptical Road')
	print('[2] Agham Road')
	print('[3] Bantayog Road')
	print('[4] Edsa')
	print('[5] SGT. Esguera')
	print('[6] Scout Albano')
	print('[7] Scout Borromeo')
	print('[8] Scout Santiago')
	print('[9] Timog')
	print('[10] Scout Reyes')
	print('[11] Scout Magbanua')
	print('[12] Roces Avenue')
	print('[13] Roosevelt Avenue')

def printEspanaPoints():
	print()
	print('[1] Welcome Rotunda')
	print('[2] Bluementritt')
	print('[3] A. Maceda')
	print('[4] Antipolo')
	print('[5] Vicente Cruz')
	print('[6] Gov. Forbes - Lacson')
	print('[7] P.Noval')
	print('[8] Lerma')

def printC5Points():
	print()
	print('[1] Tandang Sora')
	print('[2] Capitol Hills')
	print('[3] University of the Philippines')
	print('[4] C.P. Garcia')
	print('[5] Miriam College')
	print('[6] Ateneo De Manila University')
	print('[7] Xavierville')
	print('[8] Aurora Boulevard')
	print('[9] P. Tuazon')
	print('[10] Bonny Serrano')
	print('[11] Libis Flyover')
	print('[12] Eastwood')
	print('[13] Green Meadows')
	print('[14] Ortigas Ave.')
	print('[15] X C5 On-ramp')

def printOrtigasPoints():
	print()
	print('[1] Santolan')
	print('[2] Madison')
	print('[3] Roosevelt')
	print('[4] Club Filipino')
	print('[5] Wilson')
	print('[6] Connecticut')
	print('[7] La Salle Greenhills')
	print('[8] POEA')
	print('[9] EDSA Shrine')
	print('[10] San Miguel Ave')
	print('[11] as Ave.')
	print('[12] Meralco Ave')
	print('[13] Medical City')
	print('[14] Lanuza Ave')
	print('[15] Greenmeadows Ave')

def printMarcosHwyPoints():
	print()
	print('[1] SM City Marikina')
	print('[2] LRT-2 Station')
	print('[3] Dona Juana')
	print('[4] Amang Rodriguez')
	print('[5] F. Mariano Ave')
	print('[6] Robinson\'s Metro East')
	print('[7] San Benildo School')

def printRoxasBlvdPoints():
	print()
	print('[1] Anda Circle')
	print('[2] Finance Road')
	print('[3] U.N. Avenue')
	print('[4] Pedro Gil')
	print('[5] Rajah Sulayman')
	print('[6] Quirino')
	print('[7] Pablo Ocampo')
	print('[8] Buendia')
	print('[9] Edsa Extension')
	print('[10] Baclaran')
	print('[11] Airport Road')
	print('[12] Coastal Road')

def printSlexPoints():
	print()
	print('[1] Magallanes')
	print('[2] Nichols')
	print('[3] C5 On-ramp')
	print('[4] Merville Exit')
	print('[5] Bicutan Exit')
	print('[6] Sucat Exit')
	print('[7] Alabang Exit')

def getSlexPoint(point):
	if point == 1:
		return 'Magallanes'
	elif point == 2:
		return 'Nichols'
	elif point == 3:
		return 'C5 On-ramp'
	elif point == 4:
		return 'Merville Exit'
	elif point == 5:
		return 'Bicutan Exit'
	elif point == 6:
		return 'Sucat Exit'
	else:
		return 'Alabang Exit'

def getRoxasBlvdPoint(point):
	if point == 1:
		return 'Anda Circle'
	elif point == 2:
		return 'Finance Road'
	elif point == 3:
		return 'U.N. Avenue'
	elif point == 4:
		return 'Pedro Gil'
	elif point == 5:
		return 'Rajah Sulayman'
	elif point == 6:
		return 'Quirino'
	elif point == 7:
		return 'Pablo Ocampo'
	elif point == 8:
		return 'Buendia'
	elif point == 9:
		return 'Edsa Extension'
	elif point == 10:
		return 'Baclaran'
	elif point == 11:
		return 'Airport Road'
	else:
		return 'Coastal Road'


def getMarcosHwyPoint(point):
	if point == 1:
		return 'SM City Marikina'
	elif point == 2:
		return 'LRT-2 Station'
	elif point == 3:
		return 'Dona Juana'
	elif point == 4:
		return 'Amang Rodriguez'
	elif point == 5:
		return 'F. Mariano Ave'
	elif point == 6:
		return 'Robinson\'s Metro East'
	else:
		return 'San Benildo School'

def getOrtigasPoint(point):
	if point == 1:
		return 'Santolan'
	elif point == 2:
		return 'Madison'
	elif point == 3:
		return 'Roosevelt'
	elif point == 4:
		return 'Club Filipino'
	elif point == 5:
		return 'Wilson'
	elif point == 6:
		return 'Connecticut'
	elif point == 7:
		return 'La Salle Greenhills'
	elif point == 8:
		return 'POEA'
	elif point == 9:
		return 'EDSA Shrine'
	elif point == 10:
		return 'San Miguel Ave'
	elif point == 11:
		return 'as Ave.'
	elif point == 12:
		return 'Meralco Ave'
	elif point == 13:
		return 'Medical City'
	elif point == 14:
		return 'Lanuza Ave'
	else:
		return 'Greenmeadows Ave'


def getC5Point(point):
	if point == 1:
		return 'Tandang Sora'
	elif point == 2:
		return 'Capitol Hills'
	elif point == 3:
		return 'University of the Philippines'
	elif point == 4:
		return 'C.P. Garcia'
	elif point == 5:
		return 'Miriam College'
	elif point == 6:
		return 'Ateneo De Manila University'
	elif point == 7:
		return 'Xavierville'
	elif point == 8:
		return 'Aurora Boulevard'
	elif point == 9:
		return 'P. Tuazon'
	elif point == 10:
		return 'Bonny Serrano'
	elif point == 11:
		return 'Libis Flyover'
	elif point == 12:
		return 'Eastwood'
	elif point == 13:
		return 'Green Meadows'
	elif point == 14:
		return 'Ortigas Ave.'
	else:
		return 'X C5 On-ramp'

def getCommonwealthPoint(point):
	if point == 1:
		return 'Batasan'
	elif point == 2:
		return 'St. Peter\'s Church'
	elif point == 3:
		return 'Ever Gotesco'
	elif point == 4:
		return 'Diliman Preparatory School'
	elif point == 5:
		return 'Zuzuarregi'
	elif point == 6:
		return 'General Malvar Hospital'
	elif point == 7:
		return 'Tandang Sora Eastside'
	elif point == 8:
		return 'Tandang Sora Westside'
	elif point == 9:
		return 'Central Ave'
	elif point == 10:
		return 'Magsaysay Ave'
	elif point == 11:
		return 'University Ave'
	else:
		return 'Philcoa'

def getEdsaPoint(point):
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

def getQuezonAvePoint(point):
	if point == 1:
		return 'Elliptical Road'
	elif point == 2:
		return 'Agham Road'
	elif point == 3:
		return 'Bantayog Road'
	elif point == 4:
		return 'Edsa'
	elif point == 5:
		return 'SGT. Esguera'
	elif point == 6:
		return 'Scout Albano'
	elif point == 7:
		return 'Scout Borromeo'
	elif point == 8:
		return 'Scout Santiago'
	elif point == 9:
		return 'Timog'
	elif point == 10:
		return 'Scout Reyes'
	elif point == 11:
		return 'Scout Magbanua'
	elif point == 12:
		return 'Roces Avenue'
	else:
		return 'Roosevelt Avenue'

def getEspanaPoint(point):
	if point == 1:
		return 'Welcome Rotunda'
	elif point == 2:
		return 'Bluementritt'
	elif point == 3:
		return 'A. Maceda'
	elif point == 4:
		return 'Antipolo'
	elif point == 5:
		return 'Vicente Cruz'
	elif point == 6:
		return 'Gov. Forbes - Lacson'
	elif point == 7:
		return 'P.Noval'
	else:
		return 'Lerma'

def getEdsaPoint():
	road = 0
	while road < 1 or 13 < road:
		printEdsaPoints()
		road = int(input('Choose point: '))
	return getEdsaPoint(road)

def getCommonwealthPoint():
	road = 0
	while road < 1 or 13 < road:
		printCommonwealthPoints()
		road = int(input('Choose point: '))
	return getCommonwealthPoint(road)

def getQuezonAvePoint():
	road = 0
	while road < 1 or 13 < road:
		printQuezonAvePoints()
		road = int(input('Choose point: '))
	return getQuezonAvePoint(road)

def getEspanaPoint():
	road = 0
	while road < 1 or 13 < road:
		printEspanaPoints()
		road = int(input('Choose point: '))
	return getEspanaPoint(road)

def getC5Point():
	road = 0
	while road < 1 or 13 < road:
		printC5Points()
		road = int(input('Choose point: '))
	return getC5Point(road)

def getOrtigasPoint():
	road = 0
	while road < 1 or 13 < road:
		printOrtigasPoints()
		road = int(input('Choose point: '))
	return getOrtigasPoint(road)

def getMarcosHwyPoint():
	road = 0
	while road < 1 or 13 < road:
		printMarcosHwyPoints()
		road = int(input('Choose point: '))
	return getMarcosHwyPoint(road)

def getRoxasBlvdPoint():
	road = 0
	while road < 1 or 13 < road:
		printRoxasBlvdPoints()
		road = int(input('Choose point: '))
	return getRoxasBlvdPoint(road)

def getSlexPoint():
	road = 0
	while road < 1 or 13 < road:
		printSlexPoints()
		road = int(input('Choose point: '))
	return getSlexPoint(road)

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