'''
s="python program"
print(s[0])
print(s[13])
print(s[14])

print(s[-1])
print(s[-10])
print(s[-14])
print(s[-15])

print(s[0]+s[1]+s[2])
print(s[0:3])
print(s[5:13])
print(s[0:10])
print(s[0:10:2])

print(s[0:10])
print(s[10:0])
s="python program"
print(s[-10:-4])
print(s[-10:10])

print(s[10:5])
print(s[10:5:-1])

s="python program"
print(s[10:5:-1])
print(s[10:5:-1])



s="python program"
print(s[10:5])
print(s[-10:-5])

s="abcd,efgh,abcd,efgh,abcd,efgh,abcd,efgh"

2
"abcd"
"ABCD"
'''
'''
s="abcd,efgh,abcd,efgh,abcd,efgh,abcd,efgh"
i=len(s)
res=""
n_occurance=0
while i>0:
	if n_occurance==2:
		res=res+s[i::-1]
		break
	sub = s[i:i-4]
	if sub=="dcba":
		res=res+"DCBA"
		i=i-4
		n_occurance=n_occurance+1
	else:
		if i>0:
			res=res+s[i]
		i=i-1
		
print(res[::-1])
'''
s="python program"
#print(s[-11:-1:2])
#print(s[4:])
#print(s[4::-1])
#print(s[:10])
#print(s[:-10])
print(s[:10:-1])