#-*- coding: utf8 -*-

chinese_dict = {
	'1':'一',
	'2':'二',
	'3':'三',
	'4':'四',
	'5':'五',
	'6':'六',
	'7':'七',
	'8':'八',
	'9':'九',
	'0':'十'
}

def printResult(i,j,sum):
	if len(sum) > 1:
		total = chinese_dict[sum[0]] + chinese_dict[sum[1]]
	else:
		total = chinese_dict[sum[0]] 
	print '{0}乘{1}等於{2}\t\t'.format(chinese_dict[i], chinese_dict[j], total),

for j in range(1,10):
	for i in range(1,10):
		printResult(str(i), str(j), str(i*j))
	print
	
