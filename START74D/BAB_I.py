T= int(input(""))
for i in range(0,T):
    n=int(input())
    a = input("").split()
    l = [int(item) for item in a]
    for i in range(0,n):
        if l[i]<0:
            l[i]=-1*l[i]
    print(min(l)-1)
    
    