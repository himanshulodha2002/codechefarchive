T= int(input(""))
for i in range(0,T):
    n=int(input())
    a = input("").split()
    l = [int(item) for item in a]
    
    b = input("").split()
    m = [int(item) for item in b]
    
    k=l+m
    k.sort()
    #print(k)
    
    i=0
    j=0
    min=0
    d=[]
    while j<=n:
        c=k[j+n-1]-k[j]
        
        d.append(c)
        j+=1
    #print(d)
    d.sort()
    print(d[0])