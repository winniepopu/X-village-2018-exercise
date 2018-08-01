## ex3
def func(a,b):
    if b == 0:
        raise ValueError("divisor can't be zero!")
    return a/b    
try:
    num = func(2,0)
    print(num)
except Exception as e:
#    print("I'm in except block!")
    print(e)