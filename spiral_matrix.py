def fun(arr,m,n):
    i,j =0,0
    for k in range((n+1)//2):
        for a in range(n-1):
            print(arr[i][j])
            j+=1
        for a in range(m-1):
            print(arr[i][j])
            i+=1
        for a in range(n-1):
            print(arr[i][j])
            j-=1
        for a in range(m-1):
            print(arr[i][j])
            i-=1
        i+=1
        j+=1
        m-=2
        n-=2
        if m==1 and n==1:
            print(arr[i][j])
            return
        if n==1:
            for a in range(m):
                print(arr[i][j])
                i+=1
            return
        if m==1:
            for a in range(n):
                print(arr[i][j])
                j+=1
            return

