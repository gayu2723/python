def wordrev(wr):  
    let= wr.split(" ") 
    sen = [s[::-1] for s in let] 
    word = " ".join(sen) 
    return word  
wr = input() 
print(wordrev(wr)) 
