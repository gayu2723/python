def amsnot():
    u=int(input())
    l=int(input())
    for num in range(u,l+1):
        sum=0
        temp=num
        while temp>0:
            value=temp%10
            sum=sum+value**3
            temp=temp//10
        if num==sum:
            print(num)
amsnot()
