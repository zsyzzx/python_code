#! python3

import json, requests, sys

# 读取控制台命令行参数: python argv[0] argv[1].....
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()

location = ''.join(sys.argv[1:])
# 字符串格式化输出输入还不会
appid = '151691e126a1a54548d74e9b4705ba79'
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid=151691e126a1a54548d74e9b4705ba79' % (
    location)
# url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid='+appid %(location)

# 网络请求
response = requests.get(url)
response.raise_for_status()

# 加载json数据
weatherData = json.loads(response.text)

# 读取json数据，注意json数据的格式
w = weatherData['list']
city = weatherData['city']
city_name = city['name']
print('Current weather in %s' % (city_name))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print("Tomorrow:")
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print("Day after tomorrow")
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()

# print(weatherData)
