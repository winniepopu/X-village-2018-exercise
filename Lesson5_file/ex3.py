## ex3 音樂展演

import json

with open('show.json',encoding='utf-8-sig') as f:
    person = json.load(f)
    print(person)
    print(json.dumps(person, indent=4))   #可令ensure_ascii=False