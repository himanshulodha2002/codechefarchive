T= int(input())
for i in range(0,T):
    n=int(input())
    
    _ = input().split()
    a = [int(item) for item in _]
    
    __ = input().split()
    b = [int(item) for item in __]
    
    for i in range(0,n):
        if a[i]<b[i]:
            _=a[i]
            a[i]=b[i]
            b[i]=_
    
    a.sort()
    b.sort()
    maxi=a[n-1]
    mini=a[0]
    i=1
    

    fmin=[a[0]]*n
    fmax=[a[0]]*n
    lmin=[b[n-1]]*n
    lmax=[b[n-1]]*n
    
    for i in range(0,n):
        fmin[i]=min(fmin[i-1],a[i])
        fmax[i]=max(fmax[i-1],a[i])
    i=n-2    
    while i>=0:
        lmin[i]=min(lmin[i+1],b[i])
        lmax[i]=max(lmax[i+1],b[i])
        i-=1
    
    ans=maxi-mini
    j=n-1
    while j>=0:
        if(j==0):
            maxi=lmax[0]
            mini=lmin[0]
        else:
            maxi=max(fmax[j-1],lmax[j])
            mini=min(fmin[j-1],lmin[j])
        ans=min(ans,maxi-mini)
        j-=1
    print(ans)
    