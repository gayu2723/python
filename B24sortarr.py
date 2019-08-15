num=int(input())
nnum=list(map(int,input().split()))
nnum.sort()
i=0
while i<num:
    print(nnum[i],end=" ")
    i=i+1
