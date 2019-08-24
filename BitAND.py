a=int(input())
b,c=list(map(int,input().split()))[:a]
if(a<=100000):
  mul=b&c
  print(mul)
