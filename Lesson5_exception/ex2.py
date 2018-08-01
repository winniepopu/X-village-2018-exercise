## ex2 divide exception
def div(dividend, divisor):
    print("The answer is {}".format(dividend/divisor))

for i in range(5, -1, -1):
    for j in range(5, -1, -1):
        if j == 0:
            continue
        else:
            div(i, j)