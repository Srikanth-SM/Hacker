m,n=map(int,raw_input().split())
a=[]*m
b=[]*n
p=0
q=0
while(q<m):
	q+=1
	a.append(raw_input())
while(p<n):
	p+=1
	b.append(raw_input())
flag=False
# print a
# print b
for i in xrange(n):
	if not b[i] in (a[i]):
		flag=True
		break
if flag:
	print "No"
else:
	print "Yes"