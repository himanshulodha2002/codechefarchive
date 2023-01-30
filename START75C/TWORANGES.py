# cook your dish here
T= int(input(""))
for _ in range(0,T):
    
    a = input("").split()
    l = [int(item) for item in a]
    
    m=[]
    for i in range(l[0],l[1]+1):
        m.insert(i,i)
    for x in range(l[2],l[3]+1):
        if x not in m:
            m.append(x)
    
        
    print(len(m))