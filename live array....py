def live_array(a,key):
    low = 0
    high = key
    
    while low<=high:
        mid = (low+high)//2
        try:
            if a[mid]==key:
                return ('Key Found')
            elif a[mid] > key:
                high = mid-1
            else:
                low = mid+1
        except:
            high = mid-1
    return ('Key Not Present')
            
            
