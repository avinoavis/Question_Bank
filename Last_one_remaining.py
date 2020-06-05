def last_one(a):
    x =0
    while len(a)>1:
        
        if x+1 == len(a)-1:
            a.remove(a[x+1])
            x = 0
        elif x+1 == len(a)-2:
            a.remove(a[x+1])
            x = -1
        else:
            a.remove((a[x+1]))
            x +=1
        
    return a



