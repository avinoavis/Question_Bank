def binary_search(arr,low,high,key): 
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < key: 
            low = mid + 1
        elif arr[mid] > key: 
            high = mid - 1
        else: 
            return mid 
    return -1

def fun(a,key):
    l_index = None
    r_index =None
    index = binary_search(a,0,len(a)-1,key)
    if index == -1:
        return 'Key Not Found'
    l = index
    r = index
    while l !=-1:
        l = binary_search(a,0,l-1,key)
        if l != -1:
            l_index = l
    while r !=-1:
        r = binary_search(a,r+1,len(a)-1,key)
        if r != -1:
            r_index = r
    if l_index == None:
        l_index = index
    if r_index == None:
        r_index = index
        
        
    return l_index, r_index
    
print(fun([2,5,5,5,6,6,8,9,9,9],8))
