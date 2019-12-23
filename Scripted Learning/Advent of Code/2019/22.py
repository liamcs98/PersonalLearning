# https://adventofcode.com/2019/day/22


def buildDeck(Size: int) -> list:
    return list(range(0, Size))


def parseShuffleInstructions(deck: list, fileIn: str) -> list:
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


def findCardLocation(deck: list, card: int) -> int:
    return deck.index(int(card))


def dealIntoNewStack(deck: list) -> list:
    return list(reversed(deck))


def cutDeck(deck: list, cut: int) -> list:
    outDeck = deck
    if cut > 0:
        outDeck.extend(outDeck[:cut])
        return outDeck[cut:]
    elif cut < 0:
        outDeck = outDeck[cut:] + outDeck
        return outDeck[:cut]
    elif cut == 0:
        return outDeck


def dealWithIncrementN(deck: list, numb: int) -> list:
    outDeck = [0] * len(deck)
    for i, x in enumerate(deck):
        outDeck[(i * numb) % len(deck)] = x
    return outDeck


if __name__ == '__main__':
    deck = parseShuffleInstructions(buildDeck(10007), '22in.txt')
    print(findCardLocation(deck, 2019))
    # Memory Fun.
    # I lack a lot of math / number theory to make this scale.
    # https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/
    # deck2 = parseShuffleInstructions(buildDeck(119315717514047), '22in.txt')
    # print(deck2[2020])
