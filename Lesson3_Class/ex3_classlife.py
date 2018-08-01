## 建置Map Gilder
class Map:
    boader=1
    map=[]  
    
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

            
my_map=Map()
my_map.set_map(9)
my_map.set_pattern(1)
my_map.display()