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


def findBadge(groupedSacks):
    set1 = set(groupedSacks[0])
    set2 = set(groupedSacks[1])
    set3 = set(groupedSacks[2])
    return set1.intersection(set2).intersection(set3)


rucksacks = []
with open("inputs/day3.txt") as inputFile:
    for value in inputFile.readlines():
        rucksacks.append(value.strip())
# NOTES #
# a - z = 1 - 26
# A - Z = 27 - 52

totalValue = 0

# get 3 sacks
# find the common letter among the 3 sacks
# calculate the letter's value
# add to the sum
# return the sum
groupOfThree = []
for i in range(len(rucksacks)):
    groupOfThree.append(rucksacks[i])
    if (i+1) % 3 == 0:
        badge = findBadge(groupOfThree).pop()
        letterValue = getLetterValue(badge)
        totalValue += letterValue
        groupOfThree.clear()

# return the sum
print(totalValue)
