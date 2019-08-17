def value(rom): 
    if (rom == 'I'): 
        return 1
    if (rom == 'V'): 
        return 5
    if (rom == 'X'): 
        return 10
    if (rom == 'L'): 
        return 50
    if (rom == 'C'): 
        return 100
    if (rom == 'D'): 
        return 500
    if (rom == 'M'): 
        return 1000
    return -1
def r(ss): 
    res = 0
    i = 0
    while (i < len(ss)): 

        s1 = value(ss[i]) 
  
        if (i+1 < len(ss)): 

            s2 = value(ss[i+1]) 
            if (s1 >= s2): 
                res = res + s1 
                i = i + 1
            else: 
                res = res + s2 - s1 
                i = i + 2
        else: 
            res = res + s1 
            i = i + 1
    print(res)  
ni=input()
r(str(ni))
