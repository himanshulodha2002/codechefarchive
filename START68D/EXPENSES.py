T= int(input(""))
for i in range(0,T):
    a = input('').split()
    l = [int(item) for item in a]
    
    c=2**l[1]
    d=l[0]
    
    for j in range(0,d):
        c=c-(c/2)
    e=int(c)
    print(e)