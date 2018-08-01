#印出直角三角形2
n=5
a=0
while a<n:
    b=0
    while(b<n):
        if b<=(a-1):
            print(" ",end="")
        else:
            print("*",end="")
        b+=1
    print("")
    a+=1