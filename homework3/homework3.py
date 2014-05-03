# -*- coding: utf-8 -*-
import sys
import string


def readFile(fileName):
	readData = []
	with open(fileName, 'r') as read:
		readData = list(read.read().replace("\"", "").split(','))
	return readData

def getAmount(dataAfterSort):
	count = 1
	total = 0
	for data in dataAfterSort:
		amountOfEachData = reduce(lambda x,y:x+y, map(lambda x:ord(x)-ord('A')+1, data)) * count
		count = count + 1
		total = total + amountOfEachData
	return total

if __name__ == '__main__':
	inputData = readFile(sys.argv[1])
	dataAfterSort = sorted(inputData)
	total = getAmount(dataAfterSort)
	print "Total is %d " % total	
	

	