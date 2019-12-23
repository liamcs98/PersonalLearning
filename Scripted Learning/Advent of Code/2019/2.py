# https://adventofcode.com/2019/day/2

import pprint


def main():
    puzzleIn = fetchInput("2in.txt")

    # To do this, before running the program,
    # replace position 1 with the value 12 and replace position 2 with the value 2.
    # Sure..

    puzzleIn[1] = 12
    puzzleIn[2] = 2
    print(engine([1, 0, 0, 0, 99]))
    print(engine([2, 3, 0, 3, 99]))
    print(engine([2, 4, 4, 5, 99, 0]))
    print(engine([1, 1, 1, 4, 99, 5, 6, 0, 99]))
    postProcess = engine(puzzleIn)

    return postProcess[0]


def fetchInput(filename):
    # TODO clean this. One Liner?
    with open(filename) as f:
        program = [int(value) for value in f.read().split(',')]
    return program


def engine(intcode: list) -> list:
    terminate = False
    pos = 0
    
    while terminate != True:
        if intcode[pos] not in [1,2,99]:
            print('Unknown opcode {} at {}. Terminating'.format(intcode[pos], pos))
            terminate = True
        elif intcode[pos] == 1:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 1]] + intcode[intcode[pos + 2]]
            pos += 4
        elif intcode[pos] == 2:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 1]] * intcode[intcode[pos + 2]]
            pos += 4
        elif intcode[pos] == 99:
            terminate = True
            return intcode

    return intcode

if __name__ == '__main__':
    print(main())
