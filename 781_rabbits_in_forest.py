from collections import defaultdict

def numRabbits(answers):
    res, d = 0, defaultdict(int)
    for answer in answers:
        d[answer] = (d[answer] + 1) % (answer+1)
        if d[answer] == 0:
            res += answer + 1
    return res + sum([k+1 for k, v in d.items() if v != 0])


print(numRabbits([1, 1, 2]))  # 5
print(numRabbits([10, 10, 10]))  # 11
print(numRabbits([1, 0, 1, 0, 0]))  # 5
print(numRabbits([0, 0, 1, 1, 1]))  # 6
