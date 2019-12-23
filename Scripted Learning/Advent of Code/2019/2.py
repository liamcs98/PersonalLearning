# https://adventofcode.com/2019/day/2

import pprint


def main():
    intcodeMemory = fetchMemory("2in.txt")

    # To do this, before running the program,
    # replace addrition 1 with the value 12 and replace addrition 2 with the value 2.
    # Sure..

    intcodeMemory[1] = 12
    intcodeMemory[2] = 2
    print(engine([1, 0, 0, 0, 99]))
    print(engine([2, 3, 0, 3, 99]))
    print(engine([2, 4, 4, 5, 99, 0]))
    print(engine([1, 1, 1, 4, 99, 5, 6, 0, 99]))
    partOne = engine(intcodeMemory)[0]

    partTwo = 0
    for noun in range(100):
        for verb in range(100):
            intcodeMemory = fetchMemory("2in.txt")
            intcodeMemory[1] = noun
            intcodeMemory[2] = verb
            out = engine(intcodeMemory)
            if out[0] == 19690720:
                partTwo = 100*noun + verb


    return partOne, partTwo


def fetchMemory(filename):
    # TODO clean this. One Liner?
    with open(filename) as f:
        program = [int(value) for value in f.read().split(',')]
    f.close()
    return program


def engine(intcodeIn: list) -> list:
    intcode = intcodeIn
    terminate = False
    EIPAddr = 0
    acceptedInstructions = [1, 2, 99]

    while terminate != True:

        if intcode[EIPAddr] not in acceptedInstructions:
            print('Unknown opcode {} at addr {}. Terminating'.format(
                intcode[EIPAddr], EIPAddr))
            print('Accepted Instructions {}'.format(acceptedInstructions))
            terminate = True
            return intcode
        elif intcode[EIPAddr] == 1:
            parA = intcode[EIPAddr + 1]
            parB = intcode[EIPAddr + 2]
            intcode[intcode[EIPAddr + 3]] = intcode[parA] + \
                intcode[parB]
            EIPAddr += 4
        elif intcode[EIPAddr] == 2:
            parA = intcode[EIPAddr + 1]
            parB = intcode[EIPAddr + 2]
            intcode[intcode[EIPAddr + 3]] = intcode[parA] * \
                intcode[parB]
            EIPAddr += 4
        elif intcode[EIPAddr] == 99:
            terminate = True
            return intcode

    return intcode


if __name__ == '__main__':
    print(main())
