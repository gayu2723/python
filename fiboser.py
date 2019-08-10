fibo=int(input())
a=1
b=1
count=0
while(count<fibo):
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    count=count+1
