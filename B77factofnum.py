num = int(input())
nnum=[]
for i in range(1,num+1):
  if num%i==0:
     nnum.append(i)
for n in nnum:
    print(n,end=" ")   
