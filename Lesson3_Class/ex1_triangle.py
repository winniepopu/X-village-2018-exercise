## 印出直角三角形

class Shape:
    edge=1          # 也可以不用這行，python不需要初始
    def set_edge(self,n):
        self.edge=n
    def display(self):
        for i in range(self.edge):
            for j in range(0,i+1):
                print("*",end=" ")
            print("\n")

x = Shape()
x.set_edge(5)
x.display()