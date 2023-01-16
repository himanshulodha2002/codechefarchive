# cook your dish here
T= int(input())

for i in range(0,T):
    a=int(input())
    

    if a<3:
        print("LIGHT")
    if a>=3 and a<7:
        print("MODERATE")
    if a>=7:
        print("HEAVY")