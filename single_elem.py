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
            a1,a2 = a[:indx-1],a[indx+1:]
            if len(a1)%2==0:
                return sin_ele(a2)
            else:
                return sin_ele(a1)
        elif k == a[indx+1]:
            a1,a2 = a[:indx],a[indx+2:]
            if len(a1)%2==0:
                return sin_ele(a2)
            else:
                return sin_ele(a1)
        else:
            return k
            
# U can change the values of array for more test cases            
a = [1,1,2,2,3,3,4,4,5,6,6]
ans = sin_ele(a)
print(ans)
