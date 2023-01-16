T= int(input(""))
for i in range(0,T):
    a = input().split()
    l = [int(item) for item in a]
    
    b = input().split()
    n = [int(item) for item in b]
    
    m=l[0]
    k=l[1]
    
    for i in n:
        if i%k==0:
            print("YES")
            break
        
        
    else:
        for i in range(m):
            p=1 
            for j in range(i,m):
                p*=n[j]
            if p%k==0:
                print("YES")
                break
            
            
        else:
            print("NO")