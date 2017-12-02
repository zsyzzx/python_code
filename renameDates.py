#! python3
# 将文件名字中的MM-DD-YY 改成 DD-MM-YY格式

import os, re, shutil

# 正则有问题，不能正确识别有正确名称的文件
datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)?\d\d)
    (.*?)$
    """, re.VERBOSE)

# datePattern = re.compile(r"""^(.*?) # all text before the date
#     ((0|1)?\d)- # one or two digits for the month
#     ((0|1|2|3)?\d)- # one or two digits for the day
#     ((19|20)\d\d) # four digits for the year (must start with 19 or 20)
#     (.*?)$ # all text after the date
#     """, re.VERBOSE)

# 搜索文件夹中文件名, 符合要求则提取元素
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # 构建一个新文件名
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # 绝对文件路径，
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # 修改名称
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))

    # 小心使用，当代码正确后
    shutil.move(amerFilename, euroFilename)
