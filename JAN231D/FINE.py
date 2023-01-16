# cook your dish here
T= int(input())
b=[]
for i in range(0,T):
    a = int(input())
    if a<=70:
        print(0)
    if (a>70 and a<=100):
        print(500)
    if a>100:
        print(2000)