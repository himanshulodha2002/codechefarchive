T= int(input(""))
for i in range(0,T):
    
    a = input("").split()
    l = [int(item) for item in a]
    
    b=l[0]-l[1]
    
    if b<0:
        b=b*(-1)
    
    e=b/l[2]
    d=b//l[2]
    
    f=e-d
    
    if f!=0:
        d=d+1
    
    print(d)
    
    