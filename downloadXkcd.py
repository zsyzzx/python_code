#! python3
# coding=utf-8
# 　下载 xkcd网站的漫画

import requests, bs4, os

url = "https://xkcd.com/"
# url = "https://xkcd.com/3/"

os.makedirs("xkcd", exist_ok=True)

while not url.endswith('#'):
    print('Dowloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    comicElem = soup.select('#comic img')

    # for i in range(length):
    #     print(comicElem[i])
    if comicElem == []:
        print("没有图片")
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image%s....' % comicUrl)
        res_img = requests.get(comicUrl)
        res_img.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res_img.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    preLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + preLink.get('href')
print("done")
