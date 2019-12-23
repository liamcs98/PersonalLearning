# https://adventofcode.com/2019/day/2


def main():
    puzzleIn = fetchInput("2in.txt")

    # To do this, before running the program,
    # replace position 1 with the value 12 and replace position 2 with the value 2.
    # Sure..

    puzzleIn[1] = 12
    puzzleIn[2] = 2
    postProcess = engine(puzzleIn)

    return postProcess[0]


def fetchInput(filename):
    # TODO clean this
    with open(filename) as f:
        program = [int(value) for value in f.read().split(',')]
    return program


def engine(inArray):
    intcode = inArray
    position = 0
    terminate = False

    # Add len checking of pos and array catch error
    print(intcode)
    while terminate != True:
        # print(position)
        # print(intcode[position])
        # print(intcode[position + 1])
        # print(intcode[position + 2])
        # print(intcode[position + 3])

        if intcode[position] == 99:
            terminate = True
        elif intcode[position] == 1:
            s = intcode[position + 1] + intcode[position + 2]
            # print("Sum {}".format(s))
            # print("prev {}".format(intcode[position + 3]))
            intcode[position + 3] = s
            # print("after {}".format(intcode[position + 3]))
            position += 4
        elif intcode[position] == 2:
            s = intcode[position + 1] * intcode[position + 2]
            # print("multi {}".format(s))
            # print("prev {}".format(intcode[position + 3]))
            intcode[position + 3] = s
            # print("after {}".format(intcode[position + 3]))
            position += 4
        else:
            print("Unknown opcode {0} at position {1:d}.".format(
                intcode[position], position))
            terminate = True

        # print("-" * 8)
    print("-" * 8)
    print(intcode)
    print("-" * 8)

    return intcode


if __name__ == '__main__':
    print(main())
