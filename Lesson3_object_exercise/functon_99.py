#exercise1: 用func 印出 9*9 乘法表

#for
def mxm(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print (i,"*",j,"=",i*j,sep="",end='\t')
        print("\n")
mxm(9)


# -----

#while
# def MxM_table(n):
#     a=1
#     while a<=n:
#         b=1
#         while b<=n:
#             print(b,"*",a,"=",a*b,sep="",end='\t')
#             b+=1
#         print("\n")
#         a+=1

# MxM_table(9)

