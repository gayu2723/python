num=int(input())
sum=0
while(num>0):
   rev=num%10
   sum=(sum*10)+rev
   num=num//10
print(sum)   

