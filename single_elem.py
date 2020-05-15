def sin_ele(a):
    if len(a)==3:
        k = a[1]
        if k ==a[0]:
            return a[2]
        else:
            return a[0]
    else:
        indx =  len(a)//2 
        k = a[indx]
        if k == a[indx-1]:
            l = a[:indx-1]
            ll = a[indx+1:]
            if len(l)%2==0:
                return sin_ele(ll)
            else:
                return sin_ele(l)
        elif k == a[indx+1]:
            l = a[:indx]
            ll = a[indx+2:]
            if len(l)%2==0:
                return sin_ele(ll)
            else:
                return sin_ele(l)
        else:
            return k
            
# U can change the values of array for more test cases            
a = [1,1,2,2,3,3,4,4,5]
ans = sin_ele(a)
print(ans)
