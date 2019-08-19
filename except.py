from time import sleep
print("START")
a=input("enter a value:")
b=input("Enter b value:")
print(f"before converting: a={a},b={b}")
try:
    a=float(a)
    b=float(b)
    print(f"after converting: a={a},b={b}")
    sleep(10)
    res=a/b
    print(f"result={res}")
except Exception as err:
    print("this is exception as err")
except:
	print("this is except")
print("END")
print("some main block statements..")