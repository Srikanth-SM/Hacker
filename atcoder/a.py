a,b=map(int,raw_input().split())
if a==1:
	a=14
if b==1:
	b=14
 
def val():

	if(a>b):
		return "Alice"
	elif b>a:
		return "Bob"
	return "Draw"
print (val())