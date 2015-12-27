
_author__ = 'Q1mi'

'''
        猜幸运数字，num = 6
        猜的数字比6大，提示打印的小一点
        猜的数字比6小，提示打印的大一点
        猜的数字等于6，提示bingo
        猜错三次，提示too many retry
'''
luckyNum = 6
inputNum = -1
guess_count = 0
while guess_count < 3:
    inputNum = int(input("input your lucky number:"))

    if inputNum < luckyNum:
        print("You should try bigger!")
    elif inputNum > luckyNum:
        print("You should try smaller!")
    else:
        print("Bingo!")
        break
    guess_count += 1
else:
    print("Too many retry!")
