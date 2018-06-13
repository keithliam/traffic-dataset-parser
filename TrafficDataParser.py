from datetime import datetime
from time import strftime
from os.path import isfile
from os import listdir

class TrafficDataParser:
	def __init__(self, road, direction, path):
		self.road = road
		self.direction = direction
		self.path = path

	def parseDate(self, dateString):
		dateTime = datetime(int(dateString[:4]), int(dateString[4:6]), int(dateString[6:]), 0, 0)
		return dateTime.strftime('%d/%m/%Y')

	def parse(self):
		csvString = '30 Minutes,Lane 1 Flow (Veh/30 Minutes),# Lane Points,% Observed'

		filesFolders = listdir(self.path)

		for fileFolder in filesFolders:
			if isfile(self.path + fileFolder):

				
				csvString += '\n' + parseDate(fileFolder[15:23])