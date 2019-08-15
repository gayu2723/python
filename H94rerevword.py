def revword(ss):  
    let= ss.split(" ") 
    sen = [s[::-1] for s in let] 
    word = " ".join(sen) 
    return word  
ss = input() 
print(revword(ss)) 
