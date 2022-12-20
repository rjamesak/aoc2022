import collections
with open("inputs/day6.txt") as f:
    input = f.readlines()
code = input[0]

test1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test2 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

group = collections.deque(maxlen=14)
countedLetters = 0
for letter in code:
    group.append(letter)
    countedLetters += 1
    if len(group) == 14 and len(set(group)) == 14:
        print(f'counted {countedLetters} letters')
        break
