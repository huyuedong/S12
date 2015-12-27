__author__ = 'Q1mi'

luckyNum = 6
for i in range(3):
    inputNum = int(input("input your guess number:"))

    if inputNum > luckyNum:
        print("smaller!")
    elif inputNum < luckyNum:
        print("bigger!")
    else:
        print("bingo!")
else:
    print("Too many retry!")
