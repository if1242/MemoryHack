# Bing Filtration
# Version 0.1

import os
import shutil
from scripts import label_image

# каталог всех изображений, которые необходимо фильтровать
DIRECTORY_IMAGE = "bing_images/Участники_ВОВ"

# создаём каталоги для фильтрованных изображений
def create_directory(name_directory):
    try:
        os.mkdir(DIRECTORY_IMAGE + "/" + name_directory)
    except OSError:
        print("Создать директорию %s не удалось" % name_directory)
    else:
        print("Успешно создана директория %s " % name_directory)

# Получаем список имен файлов
files = os.listdir(DIRECTORY_IMAGE)

# извлекаем только имена файлов с расширениями '.bmp', '.jpg', '.jpeg', '.png', '.tif', '.tiff', '.dng'
img_files = []
for name_file in files:
    if ".bmp" in name_file or ".jpg" in name_file or ".jpeg" in name_file or ".png" in name_file \
            or ".tif" in name_file or ".tiff" in name_file or ".dng" in name_file:
        img_files.append(name_file)


directory_for_filter = ['peoplewow', 'trashwow', 'dontknow']
for name_dir in directory_for_filter:
    create_directory(name_directory=name_dir)

# фильтруем по каталогам
counter_people_wow = 0
counter_trash_wow = 0
counter_dont_know_wow = 0

for img_name in img_files:

    result_classif = label_image.run(img_name)

    if result_classif == "peoplewow":
        counter_people_wow += 1
        file_name, file_extension = os.path.splitext(img_name)
        shutil.copy(DIRECTORY_IMAGE + "/" + img_name, DIRECTORY_IMAGE + "/" + directory_for_filter[0]
                    + "/" + str(counter_people_wow) + file_extension)

    elif result_classif == "trashwow":
        counter_trash_wow += 1
        file_name, file_extension = os.path.splitext(img_name)
        shutil.copy(DIRECTORY_IMAGE + "/" + img_name, DIRECTORY_IMAGE + "/" + directory_for_filter[1]
                    + "/" + str(counter_trash_wow) + file_extension)

    elif result_classif == "dontknow":
        counter_dont_know_wow += 1
        file_name, file_extension = os.path.splitext(img_name)
        shutil.copy(DIRECTORY_IMAGE + "/" + img_name, DIRECTORY_IMAGE + "/" + directory_for_filter[2]
                    + "/" + str(counter_dont_know_wow) + file_extension)


