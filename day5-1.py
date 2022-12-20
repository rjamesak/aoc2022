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

# parse instructions for part 1
for instruction in instructions:
    count, fromStack, toStack = int(instruction[1]), int(
        instruction[3])-1, int(instruction[5])-1
    # pop fromStack into toStack (append) count times
    for i in range(count):
        stacks[toStack].append(stacks[fromStack].pop())

for stack in stacks:
    print(stack.pop())
