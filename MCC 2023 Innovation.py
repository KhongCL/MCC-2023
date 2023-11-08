N,M= map(int,input().strip().split())

listab=[]
listcd=[]
listtotal=[]
highest=0

for i in range(N):
    a,b,c,d= map(int,input().strip().split())
    listab.append(a+b)
    listcd.append(c+d)
    listtotal.append(a+b+c+d)
    
    if a+b+c+d > highest:
        highest=a+b+c+d
        hia,hib,hic,hid =a,b,c,d


for x in range(0,len(listcd)):
    if hia+hib ==listab[x-1] and hic+hid == listcd[x-1]:

          listab.remove(listab[x-1])

listab=sorted(listab,reverse=True)

point=0
counter=0

for x in range(0,M):
    if x == M-1:
        point+=max(listtotal)
        break
    point+=listab[counter]
    counter+=1


print(point)




