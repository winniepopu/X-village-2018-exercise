## ex1 八個皇后
map=[]
for i in range(8):
    row=[0,0,0,0,0,0,0,0]
    map.append(row)

def kill(l):  # 標記會被攻擊的位置為1
    x=l[0]
    y=l[1]
    #print("x: ",x,"y: ",y)

    for i in range(8):
        if i==y:
            continue
        map[x][i]=1
 
    for j in range(8):
        if j==x:
            continue       
        map[j][y]=1

        for i in range(1,8):
            if x+i<8:
                if y-i>=0:
                    map[x+i][y-i]=1
            if x+i<8:
                if y+i<8:
                    map[x+i][y+i]=1
            if x-i>=0:
                if y+i<8:
                    map[x-i][y+i]=1              
            if x-i>=0:
                if y-i>=0:
                    map[x-i][y-i]=1

def check(l): #檢查該位置是否安全
    x=l[0]
    y=l[1]
    if map[x][y]==0:
        return True 
    else:
        return False      

def eight_queens(a): #檢查大家是否皆在安全的位置
    for i in range(8):
        b=check(a[i])

        if b!=True:
            return False 
    return True 

def map_print():
    for i in range (8):
        for j in range (8):
            print(map[i][j],end=" ")
        print('')

a=[[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]

for i in range(8):
    kill(a[i]) #把會被攻擊的位置都標註起來

print(eight_queens(a)) #印出這八個皇后是否都有在安全位置
#map_print()