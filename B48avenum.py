num=int(input())
nnum=list(map(int,input().split()))[:num]
c=0
for i in range(num):
    c=c+nnum[i]
d=c//num
print(d)
