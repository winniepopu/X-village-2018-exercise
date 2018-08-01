## ex2 AQI 空氣最好的城市

import csv

with open('AQI.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    # read file row by row
    b=999
    for row in reader:
        a=row[2]  
        a=int(a)      
        if a<b:
            b=a
    b=str(b)
    
with open('AQI.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2]==b:
            print("空氣最好的城市: ",row[0],row[1],b)