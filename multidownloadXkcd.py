#! python3
# coding=utf-8
# 　多线程下载 xkcd网站的漫画

import requests, os, bs4, threading

os.makedirs('Xkcd_multi', exist_ok=True)
baseUrl = "https://xkcd.com/"


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        if urlNumber == 0:
            continue
        url = baseUrl + str(urlNumber)
        print('Downloading page %s....' % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        commicElem = soup.select('#comic img')
        if commicElem == []:
            print('没有找到图片')
        else:
            comicUrl = 'https:' + commicElem[0].get('src')
            res_img = requests.get(comicUrl)
            res_img.raise_for_status()

            imageFile = open(os.path.join('Xkcd_multi', os.path.basename(comicUrl)), 'wb')
            for chunk in res_img.iter_content(10000):
                imageFile.write(chunk)
            imageFile.close()


# 多线程代码
downloadThreads = []
# 创建线程
for i in range(0, 1900, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# 等待子线程结束
for downloadThread in downloadThreads:
    downloadThread.join()

print('done')
