## ex1 music_show
import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

with open('music_show.json','w+', encoding='utf-8-sig') as f:
    f.write(response.text)

with open('music_show.json',encoding='utf-8-sig') as f:
    res = json.load(f)    
    info=json.dumps(res,ensure_ascii=False, indent=4)

    with open('music.txt','w+',encoding='utf-8-sig')as g:

        for i in range(len(res)):
            title=res[i]['title']
            startDate=res[i]['startDate']  
            end=res[i]['endDate']
            line = "{0} : {1} ~ {2} \n".format(title,startDate,end)
            g.write(line)
