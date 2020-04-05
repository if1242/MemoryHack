# MemoryHack

# <a href="https://github.com/if1242/MemoryHack/tree/master/parsers">Выгрузка и парсинг</a>

В рамках хакатона были реализованы скрипты для выгрузки изображений по запросу из:
- Google
- Yandex
- Bing
- Flickr

Для выгрузки использовали запросы: 
- Герои ВОВ
- Участники ВОВ
- Великая Отечественная война лица
- Великая Отечественная война герои
- Дети войны
- Дети ВОВ
- Женщины в Великую Отечественную войну
- Солдаты ВОВ
- Ветераны
- Ветераны ВОВ
- Фронтовики
- Блокадники Ленинграда
- Герои блокады Ленинграда
- и т. д.

В среднем по каждому запросу можно вытащить порядка 100000 изображений. 
Для реализации парсеров был выбран <strong>язык Python</strong>, так как:
- Подходит для решения поставленной задачи
- Простой и универсальный
- Поддерживает множество библиотек 
</br>Также Python поддерживают такие гиганты IT как: Google; Dropbox; Mozilla; Facebook; Yandex; Red Hat; Microsoft; Intel; YouTube; Reddit; Instagram; PayPal; и др.

Для запуска парсера необходимо выполнить команды:</br>
<code>python google_parser.py #для Google</code></br>
<code>python bing_parser.py #для Bing</code></br>
<code>python flickr_parser.py #для Flickr</code></br>
<code>python yandex_parser.py #для Yandex</code></br>

Зависимости для корректной работы парсера прописаны в файле <a href="https://github.com/if1242/MemoryHack/blob/master/parsers/requirements.txt">requirements.txt</a>.

# <a href="https://github.com/if1242/MemoryHack/tree/master/classificator">Классификатор</a>

В данном проекте мы использовали предобученную модель <i>Inception-v3</i>, которую Google уже обучил на тысяче классов, но мы взяли наши собственные изображения. Благодаря <i>transfer learning</i>, мы смогли переобучить финальный слой уже обученной модели <i>Inception-v3</i> новым категориям с нуля. Для переобучения мы использовали <strong>Python 3 и TensorFlow 1.4.</strong> 

<strong>Причины и преимущества выбора данной технологии:</strong>
- Переобучение занимает около 30 минут на ноутбуке и не требует каких-либо графических процессоров
- У нас получилось сформировать объемный датасет для обучения (выгрузка с сайта "Дорога памяти" и из открытых источников Google, Yandex, Bing, Flickr)
- Модель уже предобучена на большом количестве классов, что увеличивает точность классификации 

В папке <a href=""><i>tf_files</i></a> мы разместили наш датасет (на github Вы видите только по одному примеру изображения из каждого класса). 
Наша модель классифицирует изображения по трем категориям: 
<ul>
<li><strong>Релевантные фото</strong> (фотографии довоенного, военного и послевоенного времени, на которых запечатлен Герой войны)</li>
<img src="classificator/tf_files/peoplewow/example.jpg" width="150px"> 
<li><strong>Фото, требующие дополнительной модерации/обработки</strong> (фото, из которых можно вырезать одного человека или фото Героя войны с текстом рядом и т.д.)</li>
<img src="classificator/tf_files/dontknow/example.jpg" width="250px"> 
  <li><strong>Спам, реклама и прочий мусор</strong></li>
<img src="classificator/tf_files/trashwow/example.jpg" width="250px"> 
</ul>

При переобучении создается новый файл графов (<i>classificator/tf_files/retrained_graph.pb</i>) и новый файл меток (<i>classificator/tf_files/retrained_labels.txt</i>). 

 Для проверки модели необходимо в каталоге <i>classificator</i> поместить изображение и выполнить:</br>
 <code>python scripts/label_image.py --image image.jpg</code>

Пример вывода модуля для релевантного изображения:</br>
<code>dontknow 0.011057022 peoplewow 0.97300134 trashwow 0.00127021</code>

Данный модуль можно использовать независимо от проекта с целью переобучения модели для любых других нужд. Благодаря гибкой архитектуре имеется возможность переобучать отличные от <i>Inception-v3</i> модели, например, модели <a href="https://ai.googleblog.com/2017/06/mobilenets-open-source-models-for.html" target="_blank"><i>Mobilenet Models</i></a> и др. В нашем проекте данный модуль играет важную роль классификации изображений при автоматической модерации. 

# <a href="https://github.com/if1242/MemoryHack/tree/master/filters">Фильтрация выгруженных изображений по каталогам</a>

В рамках хакатона был разработан <strong>модуль фильтрации на языке Python</strong>, который позволяет разносить выгруженные изображения по нужным каталогам. В процессе фильтрации для каждого источника изображений (Google/Bing итп) формируется следующая структура каталогов:
- all/ (все выгруженные изображения)
- peoplewow/ (релевантные изображения)
- dontknow/ (изображения, требующие доп модерации)
- trashwow/ (спам и прочий мусор)

В каждом каталоге можно найти <strong>файлы изображения (.png/.jpg/.gif)</strong> и <strong>метафайлы .json</strong> с информацией об источнике и о том, что изображено на картинке. 

Для запуска фильтра требуется выполнить команду:</br>
<code>python filtration_google.py #для Google</code></br>
<code>python filtration_bing.py #для Bing</code></br>

Для корректной работы модуля фильтрации требуется установить зависимости из файла <a href="https://github.com/if1242/MemoryHack/blob/master/filters/requirements.txt">requirements.txt</a>.

# UI 

# Контакты
