T= int(input(""))
output=[]

for x in range(T):
        N,A,B= map(int,input().strip().split())
        enemy=sorted(map(int,input().strip().split()),reverse=True)

        kills=0

        while A<B and enemy:

           for i in range(len(enemy)):
                if A > enemy[i]:
                        A+=enemy.pop(i)
                        kills+=1
                        break

           else:
                break
        if A>=B:
            output.append(kills)
        else:
            output.append(-1)
for x in output:
        print(x)







        

        

