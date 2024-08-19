from collections import deque

# def differ_by_one_char(s1, s2):
#     diffs = 0
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             diffs += 1
#         if diffs > 1:
#             return False
#     return diffs == 1
#
# def get_candidates(word, s_list):
#     candidates = []
#     for s in s_list:
#         if differ_by_one_char(word, s):
#             candidates.append(s)
#     return candidates

def ladderLength(beginWord, endWord, wordList):
    word_list = set(wordList)
    if endWord not in word_list:
        return 0
    ladder_length, discovered, q = 1, set(), deque([beginWord])
    while q:
        ladder_length += 1
        level_size = len(q)
        for _ in range(level_size):
            current_word = q.popleft()
            for i in range(len(current_word)):
                word_arr = list(current_word)
                for c in range(ord('a'), ord('z') + 1):
                    word_arr[i] = chr(c)
                    candidate = "".join(word_arr)
                    if candidate in word_list and candidate not in discovered:
                        if candidate == endWord:
                            return ladder_length
                        q.append(candidate)
                        discovered.add(candidate)
    return 0


print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
