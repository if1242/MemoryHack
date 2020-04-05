# Yandex Parser Image
# Version 0.1

import json
from urllib.request import urlretrieve
from selenium import webdriver
import os

search_term = 'Участники ВОВ'  # Запрос для поиска
url = "https://yandex.ru/images/search?text=" + search_term + "&ncrnd=1586010553971-7109319937478906"  # + "&source=lnms&tbm=isch"
browser = webdriver.Chrome()  # insert path to chromedriver inside parentheses
browser.get(url)
img_count = 0
extensions = {"jpg", "jpeg", "png", "gif"}

if not os.path.exists(search_term):
    os.mkdir(search_term)

for _ in range(10):
    browser.execute_script("window.scrollBy(0,100)")

html = browser.page_source.split('{')
data_yandex = []
for i in html:
    print(i)
    if i.startswith('http') and i.split('"')[0].split('.')[-1] in extensions:
        data_yandex.append(i.split('"')[0])
print(len(data_yandex))  # кол-во картинок получено для одного запроса
print(html)

i = 0
for element in data_yandex:
    try:

        url_image, url_site, title = element[0], element[1], element[2]
        if not url_image:
            url_image = "empty"
        if not url_site:
            url_site = "empty"
        if not title:
            title = "empty"

        file_name = url_image.split("/")[-1]
        # сохраняем картинку с url в папку google_images
        urlretrieve(url_image, "yandex_images/" + str(file_name))

        # формируем json
        data_json = [
            {'source_url_image': str(url_image), 'source_url_site': str(url_site), 'title': str(title)}
        ]

        # debug
        # res = json.dumps(data_json,
        #                 sort_keys=True, indent=3, separators=(',', ': '), ensure_ascii=False)
        # print(res)

        # cоздаём json файл
        file_name_not_extension, file_extension = os.path.splitext(file_name)
        with open("yandex_images/" + file_name_not_extension + str(".json"), 'w', encoding='utf8') as json_file:
            json.dump(data_json, json_file, sort_keys=True, indent=3, separators=(',', ': '), ensure_ascii=False)

        print("Загружена картинка №" + str(i))
    except:
        continue
    i += 1
