inputList = []
shapePoints = {"X": 1, "Y": 2, "Z": 3}
rock1 = "A"
paper1 = "B"
scissors1 = "C"
rock2 = "X"
paper2 = "Y"
scissors2 = "Z"
lose = "X"
draw = "Y"
win = "Z"


def getPlayer2OutcomePoints(player1, player2):
    # wins are 6 points
    if player1 == rock1 and player2 == paper2:
        return 6
    elif player1 == paper1 and player2 == scissors2:
        return 6
    elif player1 == scissors1 and player2 == rock2:
        return 6
    # ties are 3 points
    elif player1 == rock1 and player2 == rock2:
        return 3
    elif player1 == paper1 and player2 == paper2:
        return 3
    elif player1 == scissors1 and player2 == scissors2:
        return 3
    else:
        return 0


def getOtherPlayerPoints(competitorPoints):
    if competitorPoints == 0:
        return 6
    elif competitorPoints == 3:
        return 3
    else:
        return 0


winChoices = {rock1: paper2, paper1: scissors2, scissors1: rock2}
lossChoices = {rock1: scissors2, paper1: rock2, scissors1: paper2}
drawChoices = {rock1: rock2, paper1: paper2, scissors1: scissors2}


def determineChoice(player1Choice, neededOutcome):
    if neededOutcome == win:
        return winChoices[player1Choice]
    elif neededOutcome == lose:
        return lossChoices[player1Choice]
    else:
        return drawChoices[player1Choice]


# handle inputs
with open("day2Inputs.txt") as inputFile:
    inputs = inputFile.readlines()
    for input in inputs:
        curInput = input.split()
        curTuple = curInput[0], curInput[1]
        inputList.append(curTuple)
# loop each round and calc points
totalScore = 0
for round in inputList:
    player2Choice = determineChoice(round[0], round[1])
    totalScore += getPlayer2OutcomePoints(round[0], player2Choice)
    totalScore += shapePoints[player2Choice]
print(totalScore)
