## ex1 

date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')

f = open('note.txt','w+',encoding="utf-8-sig")
f.write(date)
f.write('\n')
f.write(event)
f.write('\n')
f.write(description)
f.close()