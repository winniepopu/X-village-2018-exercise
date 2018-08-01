## 製作map 有initial | Constructors

class Map:
    boader=1
    map=[]

    def __init__(self,n,p): # do initialize
        self.set_map(n)
        self.set_pattern(p)        
    
    def set_map(self,n):
        self.boader=n
        for i in range(n):
            row=[]
            for j in range(n):
                row.append("*")
            self.map.append(row)

    def set_pattern(self,p):
        n=int(self.boader/2)-1
        if p==1: #建置Gilder圖案 

            for j in range(n,n+3):
                self.map[n][j]="0"
            for i in range(n,n+2):
                self.map[i][n]="0"

            self.map[n+2][n+1]="0"

    def display(self):
        for i in range(self.boader):
            for j in range(self.boader):
                print(self.map[i][j],end=" ")
            print("\n")


n=5
p=1
my_map=Map(n,p)
my_map.display()
