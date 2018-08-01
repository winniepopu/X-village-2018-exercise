## 判斷座標在第幾象限

def where(a,b):
    if(a>0):
        if(b>0):
            print("1")
        elif(b==0) :
            print("on y")
        else:
            print("4")
    elif (a<0):
        if(b>0):
            print("2")
        elif(b==0) :
            print("on y")
        else:
            print("3")        
    else:
        print("on x")

where(-1,-10)
where(5,-5)
where(1,1)
where(-2,3)