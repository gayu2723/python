a=int(input())
c=list(map(int,input().split()))[:a]
for i in range(0,a):
    if(a<=100000):
        mul=c[i]&c[i+1]
        print(mul)
        break
    else:
        print(invalid)

