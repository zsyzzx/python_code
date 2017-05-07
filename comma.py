#coding=utf-8
'''
将一个列表元素使用', '来链接起来，并且最后的元素用'and'链接起来
'''
def comma(list):
    str = ''
    for i in range(len(list)-1):
        str +=list[i]+', '
    str += 'and '+list[-1]
    print(str)
    
spam = ['ants','cats','dogs','badgers','elephant']
comma(spam)
