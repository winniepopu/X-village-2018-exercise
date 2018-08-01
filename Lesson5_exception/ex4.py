## ex4 自己定義一個 exception 叫作 RelationException

class RelationException(Exception):
    def __init__(self,err_msg):
        self.msg=err_msg
    def __str__(self):
        return "No relationship found\n" + self.msg

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}

def check(pa, pb):
    x= pa in relation.keys()
    y= pb in relation.keys()
    if (x==False or y==False):
        raise Exception("Are you sure that {} and {} are in love with each other?".format(pa,pb))
    if relation[pa] != pb:
        raise RelationException("R U sure {} and {} have a relationship?".format(pa,pb))
    else :
        pass

try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))

except RelationException as r:
    print(r)

except Exception as e:
    print(e)