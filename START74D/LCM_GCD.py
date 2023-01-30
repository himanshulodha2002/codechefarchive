import math
T= int(input(""))
for i in range(0,T):
    
    _ = input("").split()
    l = [int(item) for item in _]
    
    b=math.gcd(l[0],l[1])
    a=l[0]
    
    
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    
    print(lcm-math.gcd(b,l[1]))