import random

def isDuplicate(array, number):
    return number in array
def lottoMaker():
    winningNumber = []

    while len(winningNumber) < 6:
        n = random.randint(1, 45)
        if n not in winningNumber:
            winningNumber.append(n)

    return winningNumber
