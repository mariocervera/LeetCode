
def maxRepeating(sequence, word):
    k = 0
    while (word * k) in sequence:
        k += 1
    return k-1


print(maxRepeating(sequence="ababc", word="ab"))  # 2
print(maxRepeating(sequence="ababc", word="ba"))  # 1
print(maxRepeating(sequence="ababc", word="ac"))  # 0
print(maxRepeating(sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba", word="aaaba"))  # 5
