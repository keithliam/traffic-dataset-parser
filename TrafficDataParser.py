from datetime import datetime
from time import strftime
from os.path import isfile, getsize
from os import listdir
import json

class TrafficDataParser:
	def __init__(self, road, direction, path):
		self.road = road
		self.direction = direction
		self.path = path

	def parseDate(self, dateString):
		dateTime = datetime(int(dateString[:4]), int(dateString[4:6]), int(dateString[6:]), 0, 0)
		return dateTime.strftime('%d/%m/%Y')

	def parseTime(self, timeString):
		time = datetime.strptime(timeString, '%I:%M %p')
		return time.strftime('%H:%M')

	def parseVolume(self, volumeString):
		if volumeString == 'light':
			return '25'
		elif volumeString == 'mod':
			return '50'
		else:
			return '75'

	def outputToCSV(self, csvString):
		fileName = self.direction + '_' + self.road.lower().replace(' ', '-').replace('.', '') + '.csv'
		file = open(fileName, 'w')
		file.write(csvString)
		file.close()

	def parse(self):
		csvString = '30 Minutes,Lane 1 Flow (Veh/30 Minutes),# Lane Points,% Observed'

		filesFolders = listdir(self.path)

		for fileFolder in filesFolders:
			if isfile(self.path + fileFolder) and getsize(self.path + fileFolder) > 0:
				fileData = json.load(open(self.path + fileFolder))
				dataPoint = next((data for data in fileData if data['line'] == self.road), None)
				if dataPoint:
					csvString += '\n' + self.parseDate(fileFolder[15:23])
					csvString += ' ' + self.parseTime(dataPoint[self.direction]['time_updated'])
					csvString += ',' + self.parseVolume(dataPoint[self.direction]['status']) + ',1,100'
		self.outputToCSV(csvString)