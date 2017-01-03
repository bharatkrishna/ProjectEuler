import math
def fib(n):
	f0,f1,f2=0,1,0
	if (n==0 or n==1) : return n
	for i in range(n-1):
		f2 = f0+f1
		f0 = f1
		f1 = f2
	return f2


n = 1
while True:
	f = fib(n)
	digits = long(math.log10(f))+1
	if digits >= 1000:
		print("#%d: %d" % (n, f))
		break
	n += 1