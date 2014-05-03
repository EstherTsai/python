# -*- coding: utf-8 -*-
import sys


def readFile(fileName):
	readArray = []
	with open(fileName, 'r') as sampleFile:
		readArray = list(sampleFile.read().splitlines())
	return readArray

def convertStringListToInt(array):
	for i in range(len(array)):
		array[i] = int(array[i])

	return array

def getThreeBiggestNumber(inputArray):
	outputArray = [inputArray[0], 0, 0]

	for i in range(1, len(inputArray)):
		if inputArray[i] > outputArray[0]:
			outputArray.insert(0, inputArray[i])
		else:
			if inputArray[i] > outputArray[1]:
				outputArray.insert(1, inputArray[i])
			else:
				if inputArray[i] > outputArray[2]:
					outputArray.insert(2, inputArray[i])

	return outputArray

def writeFile(outputArray):
	print "Output:"

	with open("output.dat", 'w') as output:
		for i in range(3):
			print outputArray[i]
			output.write((str)(outputArray[i]) + '\n')

if __name__ == '__main__':
    readArray = readFile(sys.argv[1])
    inputArray = convertStringListToInt(readArray)
    outputArray = getThreeBiggestNumber(inputArray)
    writeFile(outputArray)