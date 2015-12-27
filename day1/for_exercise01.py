__author__ = 'qimi'

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
    print("Too many retrys!")