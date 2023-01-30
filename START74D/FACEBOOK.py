T= int(input(""))
for i in range(0,T):
    n=int(input())
    a = input("").split()
    l = [int(item) for item in a]
    
    b = input("").split()
    m = [int(item) for item in b]
    c=[None]*n
    for i in range(0,n):
        c[i]=l[i]+m[i]
    max=0
    for i in range(0,n):
        if l[max]<l[i]:
            max=i
        if l[max]==l[i]:
            if c[i]>c[max]:
                max=i
    print(max+1)