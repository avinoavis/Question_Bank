def fun(arr):
    count =0
    num = min(arr[0],arr[-1])
    for i in arr:
        if i<num:
            count+=(num-i)
    return count

def water_count(array):
    n = len(array)
    i = 0
    count = 0
    while i<n-1:
        if a[i]>=a[i+1]:
            initial =i
            while (a[i] >= a[i+1]):
                i+=1
                if i == n-1:
                    return count
            while a[i] <= a[i+1]:
                i+=1
                if i == n-1:
                    break
            final = i
            count+=fun(array[initial:final+1])
        else:
            i+=1
    return count

a = [0,1,0,2,1,0,1,3,2,1,2,1]          
print(water_count(a))
        
