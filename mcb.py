#! python3
# 使用二进制文件，以类似字典的结构保存剪贴板内容
# 多重剪贴板
'''
使用说明:
py mcb.py save <keyword>  - 关键字与剪贴板内容 一一对应存到剪贴板中
py mcb.py <keyword>    - 将关键字的连接粘贴到剪贴板
py mcb.py list   - 将所有关键字保存到粘贴板

'''
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
