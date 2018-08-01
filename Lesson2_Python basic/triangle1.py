#印出直角三角形1
n=5
a=999
while a>0:
    a=n
    b=n
    while b>0:
        print("*",sep="\t",end=" ")
        b-=1
    print("")
    n-=1