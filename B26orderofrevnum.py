n=int(input())
num=list(map(int,input().split()))
num.sort()
nn=0
while nn<n:
    print(num[nn],end=" ")
    nn=nn+1
