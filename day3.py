# input: Calories
testInput = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]


def splitSackContents(sack):
    size = len(sack)
    leftSide = sack[0:size//2]
    rightSide = sack[size//2:]
    return leftSide, rightSide


def getCommonLetter(leftSide, rightSide):
    set1 = set(leftSide)
    set2 = set(rightSide)
    return set1.intersection(set2)


def getLetterValue(letter):
    ordValue = ord(letter)
    letterValue = 0
    # lowercase 1 - 26, ASCII = 97 - 122
    if ordValue in range(97, 123):
        return ordValue - 96
    # uppercase 27 - 52, ASCII = 65 - 90
    else:
        return ordValue - 38


rucksacks = []
with open("inputs/day3.txt") as inputFile:
    for value in inputFile.readlines():
        rucksacks.append(value.strip())
print(rucksacks)
# NOTES #
# a - z = 1 - 26
# A - Z = 27 - 52

totalValue = 0
for sack in rucksacks:
    # split value in half (bisect?)
    leftSide, rightSide = splitSackContents(sack)
    print(leftSide, " - ", rightSide)
    # find the value common to each half (set intersect)
    commonLetter = getCommonLetter(leftSide, rightSide).pop()
    print(commonLetter)
    # get the value of the common letter
    letterValue = getLetterValue(commonLetter)
    print(letterValue)
    # add the letter value to a running sum
    totalValue += letterValue

# return the sum
print(totalValue)
