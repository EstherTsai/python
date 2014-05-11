# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as ET

data = "<xml>" + sys.argv[1] + "</xml>"

try :
	root = ET.fromstring(data)
	print "True"

except ET.ParseError:
	 print "False"


