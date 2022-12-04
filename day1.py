# input: Calories
inputs = []
with open("input1.txt", "r") as inputFile:
    for value in inputFile.readlines():
        inputs.append(value.strip())
maxCalories = float("-inf")
calorieList = []
curSum = 0
for input in inputs:
    if (input == ""):
        maxCalories = max(curSum, maxCalories)
        curSum = 0
    else:
        curSum += int(input)
maxCalories = max(curSum, maxCalories)
print(maxCalories)

# part 2
curSum = 0
sumList = []
for input in inputs:
    if (input == ""):
        sumList.append(curSum)
        curSum = 0
    else:
        curSum += int(input)
sumList.append(curSum)
sumList.sort()
top3Sum = 0
for i in range(3):
    top3Sum += sumList.pop()
print(top3Sum)
