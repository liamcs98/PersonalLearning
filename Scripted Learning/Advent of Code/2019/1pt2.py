# https://adventofcode.com/2019/day/1

import math


def main():
    puzzleIn = fetchInput("1in.txt")
    answer = 0
    for x in puzzleIn:
        answer += findFuel(x)

        secondFuelMass = findFuel(x)
        fuelmass = 0 
        while findFuel(secondFuelMass) > 0:
            fuelmass += findFuel(secondFuelMass)
            secondFuelMass = findFuel(secondFuelMass)

        answer += fuelmass


    return answer


def fetchInput(filename):
    file = open(filename, "r")
    out = []
    for line in file:
        out.append(int(line))
    return out


def findFuel(a):
    return (math.floor((a / 3)) - 2)


if __name__ == '__main__':
    print(main())
