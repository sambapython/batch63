'''
def fun(x):
	if x%2==0:
		return "EVEN"
	else:
		return "ODD"
res=fun
print(res)
'''
'''
x=1000
def fun(a,b):
	x=2000
	print("inside fun x=",x)
print("outdie the fun x=",x)
fun(100,200)
'''
x=1000
y=2000
print(f"before fun call:x={x},y={y}")
def fun(a,b):
	x=a+b
	print(f"inside fun x={x}, y={y}")
fun(100,200)
print(f"after fun call:x={x},y={y}")
fun(1,2)
print(f"after second fun call:x={x},y={y}")