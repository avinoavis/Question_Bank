def last_one(a):
    x =0
    while len(a)>1:
        try:
            a.remove(a[x+1])
            x = x+1
        except:
            x = -1
    return a


