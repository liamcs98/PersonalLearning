# https://adventofcode.com/2019/day/4
import re

def containsAdjacent(passcode: int) -> bool:
    for i, x in enumerate(str(passcode)):
        try:
            if x == str(passcode)[i + 1]:
                return True
        except IndexError:
            pass
    else:
        return False


def neverdecrease(passcode: int) -> bool:
    for i, x in enumerate(str(passcode)):
        try:
            if x > str(passcode)[i + 1]:
                return False
        except IndexError:
            pass
    else:
        return True

if __name__ == '__main__':
    count = 0
    for i in range(256310, 732736):
        if containsAdjacent(i) and neverdecrease(i):
            count += 1
    print(count)
