## 巴斯卡三角形

def cal(n):
    if(n==0):
        return 1
    if(n==1):
        return n
    else:
        return n*cal(n-1)


def C(a,b):
    x=cal(a)/(cal(b)*cal(a-b))
    return x

def n_m(a,b):
    x=C(a-1,b-1)
    return int(x)


n=input("please enter n: ")
n=int(n)
n+=1
for i in range(1,n):
    for j in range(1,i+1):
        if(j==1):
            for k in range(1,n-i):
                print(" ",end="  ")
        print(n_m(i,j),end="     ")
    print("\n")  