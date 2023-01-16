# cook your dish here
T= int(input(""))
for i in range(0,T):
    a = input("").split()
    l = [int(item) for item in a]
    
    m=l[0]
    k=l[1]
    
    b=(m*(m+1))//2
    if k<b:
        print(-1)
    else:
        for i in range(m-1):
            print(1,end=" ")
        print(k-b+1)
