#! python3

'''
从剪贴板读取字符串，并提取出中的电话号码和邮箱，在控制台输出结果，并复制到剪贴板中

不足:
没有提取出手机号
没有对国内号码做适配
'''

import re, pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # 区号
    (\s|-|\.)?            #连接符
    (\d{3})              #三数字
    (\s|-|.)             #连接符
    (\d{4})             # 4数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 拓展
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  #username
    @
    [a-zA-Z0-9.-]+  #domain name
    (\.[a-zA-Z]{2,4}){1,2}
    )''', re.VERBOSE)

# text = str(tempstr)
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone or email found ')
