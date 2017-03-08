#coding=utf-8
'''
输入整数：如果是奇数，则输出3*num+1
如果是偶数则输出num/2
如果循环调用，最后肯定变成1
'''

def collatz(number):
    if number%2 == 0:
        print(number/2)
        return number/2
    else:
        print (number*3+1)
        return number*3+1

print("请输入数字:")
temp = int(input())
while temp != 1:
    temp = collatz(temp)
