n1,n2=list(map(int,input().strip().split()))[:2]
n1,n2= (n1^n2)^((n1^n2)^n2),(n1^n2)^n2
print(n1,n2)
