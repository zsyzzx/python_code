#! python3
# coding=utf-8

# lucky.py 打开若干个前面搜索结果

'''
只支持Google搜索，而且要开全局翻墙
尝试了百度和bing搜索，但对html标签不熟悉和链接不熟悉
不能找到正确的链接并打开
'''

import sys, bs4, requests, webbrowser

print('Googling')
test_url = 'https://Google.com/search?q=' + ''.join(sys.argv[1:])
res = requests.get(test_url)  # 使用requests模块请求链接，并下载下来
test = res.raise_for_status()  # 出错停止,抛出错误码，更多资料看：requests官方文档
print(test)

# 找到链接
soup = bs4.BeautifulSoup(res.text, "html.parser")  # 使用bs4解析下载的html文件
# 打开链接
linkElems = soup.select('.r a')  # 识别html标签，.r class 下的 a标签
numOpen = min(5, len(linkElems))  # 打开前5个搜索链接
for i in range(numOpen):
    webbrowser.open('https://Google.com' + linkElems[i].get('href'))
webbrowser.open(test_url)  # 使用系统浏览器打开
