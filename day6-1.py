import collections
with open("inputs/day6.txt") as f:
    input = f.readlines()
code = input[0]

test1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test2 = "nppdvjthqldpwncqszvftbrmjlhg"
test3 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

group = collections.deque(maxlen=4)
countedLetters = 0
for letter in code:
    group.append(letter)
    countedLetters += 1
    if len(group) == 4 and len(set(group)) == 4:
        print(f'counted {countedLetters} letters')
        break
