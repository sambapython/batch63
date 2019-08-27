def outer():
	print("this is outer")
	def inner():
		print("this is inner")
	return 20
res=outer
print("result=",res)