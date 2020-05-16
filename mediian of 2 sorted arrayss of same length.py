def mediann(a):
    if len(a)%2 ==0:
        l = len(a)//2
        return (a[l]+a[l-1])/2
    else:
        return a[len(a)//2]
def med_ar(a,b):
    while len(a)>2:
        if  mediann(a)==mediann(b):
            return mediann(a)
        elif mediann(a)>mediann(b):
            a = a[:len(a)//2 + 1]
            b = b[(len(b)-1)//2:]
        else:
            a = a[(len(a)-1)//2:]
            b = b[:len(b)//2 + 1]
    return (max(a[0],b[0])+min(a[1],b[1]))/2    
        

a = [2,6,12,20,24,30]
b = [1,4,7,13,19,20]
print(med_ar(a,b))
