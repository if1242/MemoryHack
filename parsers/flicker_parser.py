# Flickr Parser Image
# Version 0.1

import argparse
import os
import time

import requests
from flickrapi import FlickrAPI

key = 'Из телеги в канале, либо по ссылке справа получить новый'  # Flickr API key https://www.flickr.com/services/apps/create/apply
secret = 'Из телеги в канале, либо по ссылке справа получить новый'


def download_uri(uri, dir='./'):
    with open(dir + uri.split('/')[-1], 'wb') as f:
        f.write(requests.get(uri, stream=True).content)


def get_urls(search='honeybees on flowers', n=10, download=False):
    t = time.time()
    flickr = FlickrAPI(key, secret)
    photos = flickr.walk(text=search,  # http://www.flickr.com/services/api/flickr.photos.search.html
                         extras='url_o',
                         per_page=100,
                         sort='relevance')

    if download:
        dir = os.getcwd() + os.sep + 'images' + os.sep + search.replace(' ', '_') + os.sep  # save directory
        if not os.path.exists(dir):
            os.makedirs(dir)

    urls = []
    for i, photo in enumerate(photos):
        if i == n:
            break

        try:
            # construct url https://www.flickr.com/services/api/misc.urls.html
            url = photo.get('url_o')  # original size
            if url is None:
                url = 'https://farm%s.staticflickr.com/%s/%s_%s_b.jpg' % \
                      (photo.get('farm'), photo.get('server'), photo.get('id'), photo.get('secret'))  # large size

            # download
            if download:
                download_uri(url, dir)

            urls.append(url)
            print('%g/%g %s' % (i, n, url))
        except:
            print('%g/%g error...' % (i, n))

    # import pandas as pd
    # urls = pd.Series(urls)
    # urls.to_csv(search + "_urls.csv")
    print('Done. (%.1fs)' % (time.time() - t) + ('\nAll images saved to %s' % dir if download else ''))


if __name__ == '__main__':
    get_urls(search='Великая Отечественная Война',  # Запроса для поиска
             n=100,  # Максимальное количество картинок
             download=True)  # Скачать: True/False
