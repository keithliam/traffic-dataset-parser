from datetime import datetime
from time import strftime
from os.path import isfile, getsize
from os import listdir
from math import ceil
from random import shuffle
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

	def parse(self):
		dataList = []

		filesFolders = listdir(self.path)

		for fileFolder in filesFolders:
			if isfile(self.path + fileFolder) and getsize(self.path + fileFolder) > 0:
				fileData = json.load(open(self.path + fileFolder))
				dataPoint = next((data for data in fileData if data['line'] == self.road), None)
				if dataPoint:
					elementString = self.parseDate(fileFolder[15:23])
					elementString += ' ' + self.parseTime(dataPoint[self.direction]['time_updated'])
					elementString += ',' + self.parseVolume(dataPoint[self.direction]['status']) + ',1,100'
					dataList.append(elementString)
		return dataList

	def getFilename(self):
		return self.direction + '_' + self.road.lower().replace(' ', '-').replace('.', '')

	def trainTestSplit(self, dataset, testPercent):
		dataset = list(dataset)
		shuffle(dataset)
		trainLen = len(dataset) - ceil(testPercent * len(dataset))
		return dataset[0:trainLen], dataset[trainLen:len(dataset)]