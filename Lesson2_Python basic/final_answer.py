## 終極密碼

import random
answer = random.randint(1,100)
a=0
while(a!=answer):
    a=input("enter a number")
    a=int(a)
    if a>answer:
        print("too big")
    elif a<answer:
        print("too small")
    else:
        print("you got it")