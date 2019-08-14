a=1
b=2
def supplier_create():
	print("supplier created successfully")
def main1():
	def fun1():
		print("this is fun1 in pur")
	print("this is purchase")
	supplier_create()
	fun1()
if __name__ == "__main__":
	main1()
	