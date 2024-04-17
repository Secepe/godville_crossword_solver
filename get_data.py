from bs4 import BeautifulSoup
import requests

dick = {0:'Монстры', 1:'Трофеи', 2:'Умения', 3:'Снаряжение', 4:'Боссы',
        5: 'Города', 6:'Местности', 7:'Твари'}

a = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
x = ['%23',"120F9FGV90F889"]
for i in a:
    x.append(i)
def save_data(n):
    item_names = []
    for i in x:
        url = "https://gv.erinome.net/db?type="+str(n)+"&lang=ru&letter="+i
        response = requests.get(url)
        bs = BeautifulSoup(response.text,"html")
        temp_list = bs.find_all('span', 'itemname')
        for temp in temp_list:
            item_names.append(temp.text)
            
    item_names = str(item_names)
    fp = "S:\\datas\\" +dick[n] +'.txt' # Изменить на свой путь

    with open(fp, "w", encoding='utf-16') as file:
            file.write(item_names)
for i in dick:
     save_data(i)