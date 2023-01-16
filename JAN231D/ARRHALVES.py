T= int(input())
for i in range(0,T):
    xi=[]
    yi=[]
    n=int(input())
    
    b = input().split()
    m = [int(item) for item in b]
    
    x=m[:n]
    y=m[n:]
    
    for i in range(0,n):
        if x[i]>n:
            xi.append(i+1)
        
    for j in range(0,n):
        if (y[j]<=n):
            yi.append(j+n+1)
    ans=0
            
    for k in range(0,len(xi)):
        ans+=yi[k]-xi[k]
    print(ans)  
    