# -*- coding: utf-8 -*-
import re
import sys
import xml.etree.ElementTree as ET

inputData =  "<a><a></a><a></a></a>"
#sys.argv[1]

xmlData = "<xml>" + inputData + "</xml>"
print xmlData

try :
	root = ET.fromstring(xmlData)
	for each in root:
		print each.tag

	# print "True"

except:
	 print "False"


