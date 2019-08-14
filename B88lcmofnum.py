nnum1,nnum2=map(int,input().split())
lcmnum = nnum1 if(nnum1 > nnum2) else nnum2
while(True):
    if((lcmnum % nnum1 == 0) and (lcmnum % nnum2 == 0)):
        print(lcmnum)
        break
    lcm =lcmnum + 1
