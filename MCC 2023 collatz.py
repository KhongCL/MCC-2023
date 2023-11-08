in1= str(input(""))
for u in in1:
    if u == " ":
        in1= int(in1[in1.index(u):])


in2=str(input(""))
list=[]

counter=0
counter2=0


while counter2 < len(in2)+1:
       
   if counter2 == len(in2):
        list.append(int(in2[counter2-counter:]))
        break
       
          

   if in2[counter2] == " ":
          index2= counter2
          index1= index2-counter
          list.append(int(in2[index1:index2]))
          counter=0
          counter2+=1

   else:
            counter +=1
            counter2+=1
for x in range(in1):
   counter3=0
   for i in list:
    if i %2==0:
        list[counter3]= i/2
    else:
        list[counter3]= (3*i) +1
    counter3+=1

print(round(sum(list)))