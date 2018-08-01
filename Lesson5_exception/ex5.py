## 小明買醬油

import random
item_in_shop = {"soybean_sauce": 0, "milk": 4, "salt": 10, "soybean_milk": 3}
items = [item for item in item_in_shop.keys()]
cnt = 5

def buy(item):
    if item_in_shop[item]==0:
        raise Exception("There's no {}".format(item))
    else:
        item_in_shop[item]-=1

    # tips: 如果東西數量是 0 需要 raise Exception,否則就把物品的數量減 1 
    print("Mommy! I've bought {} for you!".format(item))

# 買五個隨機的東西
while cnt:
    cnt -= 1
    index = random.randint(0,3)
    item = items[index]

    try:
        buy(item)

    except Exception as e:
       # print("I'm in except block")
        print(e)