#! python3
# 秒表，按下回车开始，回车记圈

import time

print('回车开始，开始后，回车键来记圈数 ctrl+c 退出')
# 初始化，记录开始时间
input()
print('started')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        # 计时逻辑
        input()
        nowTime = time.time()
        lapTIme = round(nowTime - lastTime, 2)
        totalTime = round(nowTime - startTime, 2)

        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTIme), end='')

        # 更新数据
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('计数结束')
