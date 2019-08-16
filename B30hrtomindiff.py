hr1,min1=list(map(int,input().split()))
hr2,min2=list(map(int,input().split()))
hr=hr1-hr2
min=min1-min2
print(abs(hr),abs(min))
