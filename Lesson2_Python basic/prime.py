## 印出1~50的質數
n=50
print("in 1 ~",n,", prime : ")
for i in range(2,n):
    for j in range (2,i):
        if(i%j==0):
            break
    else: 
        print(i,end=" ")