T= int(input(""))
for i in range(0,T):
    n=int(input())
    a = input("").split()
    l = [int(item) for item in a]
    
    c=0
    for i in range(0,n):
        if l[i]==0:
            c+=1
            
    if c%2==0:
        print("YES")
    else:
        print("NO")