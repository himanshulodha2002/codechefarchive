T= int(input(""))
for i in range(0,T):
    a = input('').split()
    l = [int(item) for item in a]
    
    c= l[1]-l[0]
    

    if c>0:
        print("PROFIT")
    if c==0:
        print("NEUTRAL")
    if c<0:
        print("LOSS")
