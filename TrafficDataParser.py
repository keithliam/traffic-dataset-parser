from os.path import isfile
from os import listdir

class TrafficDataParser:
	def __init__(self, road, direction):
		self.road = road
		self.direction = direction
		self.path = path

	def parse(self):
		csvString = '30 Minutes,Lane 1 Flow (Veh/30 Minutes),# Lane Points,% Observed'

		filesFolders = listdir(self.path)

		for fileFolder in filesFolders:
			if isfile(self.path + fileFolder):
				csvString += '\n' + parseDate(fileFolder[15:23])