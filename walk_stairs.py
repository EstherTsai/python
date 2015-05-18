# -*- coding: utf-8 -*-
#[程式題]Forward_Iterative_Method 
#有一個樓梯，你每次只能爬 1 階、2 階。
#請寫一個 function，傳入樓梯總長為 N 階，回傳總共有多少種走法，且印出每種走法。
#例如：樓梯總長為 5 階，走法有「1,1,1,1,1」、「1,1,1,2」、「1,2,2」、「1,1,2,1」、「1,2,1,1」，「2,1,1,1」、「2,2,1」、「2,1,2」共 8 種
# 1.在 Python 中，一个变量保存的值除了基本类型保存的是值外，其它都是引用(指保存的值为对象的地址)，因此对于它们的使用要注意。
# 2.如果是nested list時，必須使用copy.deepcopy才能完整複製list.


# -*- coding: utf-8 -*-
from copy import deepcopy
import sys

def f(n):
	path1 = [[1]]
	path2 = [[1,1],[2]]

	for k in range (3,n+1):
		temp1 = deepcopy(path1)
		temp2 = deepcopy(path2)

		for i in range (len(temp1)):
			temp1[i].append(2)

		for j in range (len(temp2)):
			temp2[j].append(1)

		result = temp1 + temp2

		path1 = path2
		path2 = result

	
	for i in result:
		print i
	print '共 %d 種走法' % (len(result))


f(10)
