#[程式題] 最近看到一個不錯的題目，大家可以試試看：
#有一個樓梯，你每次只能爬 1 階、3 階，或 5 階。請寫一個 function，傳入樓梯總長為 N 階，回傳總共有多少種走法。
#例如：樓梯總長為 5 階，走法有「1、1、1、1、1」、「5」、「1、3、1」、「1、1、3」、「3、1、1」，共 5 種
#(注意：要剛好走完、不得超過總長，且不能後退)

import sys

# sys.setrecursionlimit(10000)

def f(n):
	if n < 0:
		return 0  
	elif n==0 or n==1 or n==2:
		fn[n] = 1
		return fn[n]
	else:
		if fn[n] == None:
			fn[n] = f(n-1) + f(n-3) + f(n-5)
		return fn[n]

fn = [None] * (50 + 1)
print f(50)
