import numbers
T= int(input(""))
for i in range(0,T):
    a = input('').split()
    l = [int(item) for item in a]
    
    d=l[1]-l[0]
    c=((l[0]+l[1])/2)
    e=int(c)
    f=c-e
    if f==0:
        print(e)
    else:
        print("-1")
    
        
   