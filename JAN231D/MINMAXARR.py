def solve(n,m,mid):
    l=m.copy()
    if l[0]>mid:
        return False
    for i in range(1,n):
        if l[i-1]<mid:
            _=mid-l[i-1]
            l[i-1]=mid
            l[i]= l[i]-_
        if l[i]>mid:
            return False
    #maxi=max(l)
    if max(l)>mid:
        return False
    
    
    
    return True



T= int(input())
for _ in range(0,T):
    n=int(input())
    b = input().split()
    m = [int(item) for item in b]
    j = max(m)
    i=0
    ans= 1e9
    while i<=j:
        mid= i+(j-i)//2
        if(solve(n,m,mid)):
            ans=min(ans,mid)
            j=mid-1
        else:
            i=mid+1
    print(ans)