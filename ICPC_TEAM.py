tests=input()

# print a
# print a[0],a[1]
i=0
dic={}
while i < tests:
    j=0
    i=i+1
    found=0
    a=raw_input().split(" ")
    # print a
    while j<int(a[0]):
        # if(int(a[1])==1):
        #     break

        j+=1
        st=len(raw_input())
        dic[st]=dic.get(st,0)+1
        # print "sdasd",a[1]
        for e in dic.keys():
            # print a[1]!=1 and dic[e]!=int(a[1])
            if(int(a[1])!=1 and dic[e]!=int(a[1])):
                found=1
    if found==1 :
        print "Not possible"
    else:
        print "Possible"
