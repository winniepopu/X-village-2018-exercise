
## ex2 交換數字
## change number

def change(a,b):
    tmp=a
    a=b
    b=tmp
    return (a,b)

a=input("enter a: ")
b=input("enter b: ")
print(a," ",b)
(a,b)=change(a,b)
print(a," ",b)