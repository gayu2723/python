num=int(input())
n1=list(map(int,input().split()))
c=[1]*num
for i in range(num):
    if(i==0):
        if n1[i]>n1[i+1]:
            c[i]+=c[i+1]
    else:
        if n1[i]>n1[i-1]:
            c[i]+=c[i-1]
print(sum(c))
