def catalan(num): 
    if num <=1 : 
        return 1 
   
    cat = 0 
    for n in range(num): 
        cat =cat+ catalan(n) * catalan(num-n-1) 
  
    return cat 
nnum=int(input())
for n in range(nnum+1): 
    print(catalan(n),end=" ") 
