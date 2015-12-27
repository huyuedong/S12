__author__ = 'qimi'
'''
    猜幸运数字，num = 6
    猜的数字比6大，提示打印的小一点
    猜的数字比6小，提示打印的大一点
    猜的数字等于6，提示bingo
'''
luckyNum = 6
inputNum = -1
while inputNum != luckyNum:
    inputNum = int(input("input your lucky number:"))

    if inputNum < luckyNum:
        print("You should try bigger!")
    elif inputNum > luckyNum:
        print("You should try smaller!")
print("Bingo!")
