def mediann_2arr(a,b):
    
    if len(a)>len(b):
        a ,b = b ,a
    n = len(a)
    m = len(b)
    low = 0
    high = n
    median =0
    while(low<=high):
        mid_a = (low+high)//2
        mid_b = (n+m+1)//2 -mid_a

        if mid_a>0 and mid_b<m and a[mid_a-1]>b[mid_b]:
            high = mid_a-1
        elif mid_a<n and mid_b>0 and a[mid_a]<b[mid_b-1]:
            low = mid_a+1
        else:
            if (mid_a==0):
                median = b[mid_b-1]
            elif mid_b ==0:
                median = a[mid_a-1]
            else:
                median = max(a[mid_a-1],b[mid_b-1])
            break
    if (n+m)%2 ==1:
        return median
    if mid_a==n:
        return (median +b[mid_b])/2
    if mid_b ==m:
        return (median +a[mid_a])/2
    return (median + min(a[mid_a],b[mid_b]))/2

a = [1,2,3,4]
b = [1,2]
print(mediann_2arr(a,b))

