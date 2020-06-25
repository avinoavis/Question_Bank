import math

def hour_counter(k,p,H):
    hour = 0 
    for i in p:
        hour += math.ceil(i/k)
        if hour> H:
            return hour
    return hour

def fun2(l,h):
    if h == -1:
        a = [i for i in range(1,p[l]+1)]
    else:
        a = [i for i in range(p[h],p[l]+1)]
    return fun(a,H)

def fun(a,H):
    n = len(a)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        h = hour_counter(a[mid],p,H)
        if h<H:
            high = mid-1
        if h>H:
            low = mid +1
        if h == H:
            return a[mid]
    return fun2(low,high)

p = [30,11,23,4,20]
H =6
p.sort()
print(fun(p,H))
            

