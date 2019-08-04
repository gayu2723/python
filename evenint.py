def evenint():
    s=int(input())
    e=int(input())
    i=0
    for i in range(s,e+2):
        if(i%2==0):
           print(i,end=" ")
evenint()
        
