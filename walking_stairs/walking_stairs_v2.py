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
