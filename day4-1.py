

inputs = []
with open("inputs/day4.txt") as inputFile:
    for value in inputFile.readlines():
        inputs.append(value.strip().split(","))


def rangeIsFullyContained(start1, end1, start2, end2):
    # check 2 in 1
    if (start1 <= start2 and end1 >= end2):
        return True
    # check 1 in 2
    elif (start2 <= start1 and end2 >= end1):
        return True
    else:
        return False


totalCount = 0
for input in inputs:
    range1 = input[0].split("-")
    range2 = input[1].split("-")
    start1, end1 = int(range1[0]), int(range1[1])
    start2, end2 = int(range2[0]), int(range2[1])
    if rangeIsFullyContained(start1, end1, start2, end2):
        totalCount += 1

print(totalCount)
