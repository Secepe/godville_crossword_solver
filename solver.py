import re

a = ('Монстры.txt', 'Твари.txt', 'Города.txt',
'Боссы.txt', 'Местности.txt', 'Снаряжение.txt',
'Умения.txt', 'Трофеи.txt')
fp = "S:\\datas\\" # Изменить на папку с сохраненными словами
R = r'во.о.онный' # Изменить на нужное слово
for i in a:
    with open(fp+i,'r',encoding='utf-16') as file:
        content = file.read()
        content = content.split(',')
        rq = re.compile(R, re.IGNORECASE)
        for word in content:
            if re.search(rq, word):
                print(word)

