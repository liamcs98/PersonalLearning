# https://adventofcode.com/2019/day/22


def buildDeck(intSize):
    return list(range(0, intSize))


def parseShuffleInstructions(deck, fileIn):
    file_obj = open(fileIn, "r")
    outDeck = deck
    for x in file_obj:
        if x.rstrip() == "deal into new stack":
            outDeck = dealIntoNewStack(outDeck)
        elif x[0] == 'c':
            s = x.rstrip()
            outDeck = cutDeck(outDeck, int(s[4:]))
        elif x[0] == 'd':
            s = x.rstrip()
            outDeck = dealWithIncrementN(outDeck, int(s[20:]))
    return outDeck


def findCardLocation(deck, cardInt):
    return deck.index(int(cardInt))


def dealIntoNewStack(deck):
    return list(reversed(deck))


def cutDeck(deck, cutInt):
    outDeck = deck
    if int(cutInt) > 0:
        outDeck.extend(outDeck[:cutInt])
        return outDeck[cutInt:]
    elif int(cutInt) < 0:
        outDeck = outDeck[cutInt:] + outDeck
        return outDeck[:cutInt]
    elif int(cutInt) == 0:
        return outDeck


def dealWithIncrementN(deck, numb):
    outDeck = [0] * len(deck)
    for i, x in enumerate(deck):
        outDeck[(i * numb) % len(deck)] = x
    return outDeck


if __name__ == '__main__':
    deck = parseShuffleInstructions(buildDeck(10007), '22in.txt')
    print(findCardLocation(deck, 2019))
    # Memory Fun.g
    # I lack a lot of math / number theory to make this scale.
    # https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/
    # deck2 = parseShuffleInstructions(buildDeck(119315717514047), '22in.txt')
    # print(deck2[2020])
