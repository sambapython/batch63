a=1000
b=2000
c=a+b
print(a,b,c)
for i in [1,2,0,4,5]:
	if i!=0:
		print(10/i)

def fun(x,y):
	try:
		print(x)
		print(y)
		res=x+y
		return res
	except Exception as err:
		print(err)
print("hello")
import pdb;pdb.set_trace()
fun(10,20)
print("end")