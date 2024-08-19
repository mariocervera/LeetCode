from collections import Counter


def maxScoreWords(words, letters, score):
    n = len(words)
    max_score = 0
    scores = [sum([score[ord(c)-ord('a')] for c in word]) for word in words]

    def backtrack(i, current_score, letter_counter):
        nonlocal max_score
        if i == n:
            max_score = max(max_score, current_score)
            return
        for b in (True, False):
            if b:
                word = words[i]
                valid_word = True
                for c in word:
                    if not letter_counter[c]:
                        valid_word = False
                    letter_counter[c] -= 1
                if valid_word:
                    backtrack(i+1, current_score + scores[i], letter_counter)
                for c in word:
                    letter_counter[c] += 1
            else:
                backtrack(i+1, current_score, letter_counter)

    backtrack(0, 0, Counter(letters))

    return max_score


print(maxScoreWords(
    ["dog", "cat", "dad", "good"],
    ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
    [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # 23

print(maxScoreWords(
    ["xxxz", "ax", "bx", "cx"],
    ["z", "a", "b", "c", "x", "x", "x"],
    [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]))  # 27

print(maxScoreWords(
    ["leetcode"],
    ["l", "e", "t", "c", "o", "d"],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]))  # 0
