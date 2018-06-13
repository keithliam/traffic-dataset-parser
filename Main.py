def printRoadChoices():
	print('[1] EDSA')
	pirnt('[2] Commonwealth')
	print('[3] Quezon Avenue')
	print('[4] España')
	print('[5] C5')
	print('[6] Ortigas')
	print('[7] Marcos Highway')
	print('[8] Roxas Blvd.')
	print('[9] SLEX')

def printDirectionChoices():
	print('[1] Northbound')
	print('[2] Southbound')

def getRoad():
	road = 0
	while road < 1 and 9 < road:
		printRoadChoices()
		road = int(input('Choose road: '))
	return road

def getDirection():
	direction = 0
	while direction < 1 and 2 < direction:
		printDirectionChoices()
		direction = int(input('Choose direction: '))
	return direction