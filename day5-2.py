import re

wholeStack = []
with open("inputs/day5Stack.txt") as inputFile:
    for value in inputFile.readlines():
        tabsReplaced = value.replace("    ", " x ")
        result = tabsReplaced.split()
        wholeStack.append(result)
wholeStack.pop()

# create empty stacks
stacks = []
for i in range(9):
    stacks.append([])

# populate stacks
for row in wholeStack:
    for i in range(len(row)):
        if row[i] != "x":
            stacks[i].insert(0, row[i])

# get instructions
instructions = []
with open("inputs/day5Instructions.txt") as inputFile:
    for value in inputFile.readlines():
        instructions.append(value.split())


def getStackSlice(count, fromStack):
    newFromStack = stacks[fromStack][slice(-count)]
    crates = stacks[fromStack][-count:]
    return newFromStack, crates


# parse instructions for part 2
for instruction in instructions:
    count, fromStack, toStack = int(instruction[1]), int(
        instruction[3])-1, int(instruction[5])-1
    # pop a slice from one stack to another
    newFromStack, crates = getStackSlice(count, fromStack)
    # replace fromStack
    stacks[fromStack] = newFromStack
    for crate in crates:
        stacks[toStack].append(crate)

for stack in stacks:
    print(stack.pop())
