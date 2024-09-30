from functools import lru_cache


def validSequence(word1, word2):
    m, n = len(word1), len(word2)

    @lru_cache(maxsize=None)
    def backtrack(word1_index, word2_index, change_available):
        if word2_index == n:
            return [], True  # Success

        if word1_index == m:
            return [], False  # Failure

        if word1[word1_index] == word2[word2_index]:
            indices, success = backtrack(word1_index + 1, word2_index + 1, change_available)
            if success:
                indices.append(word1_index)
            return indices, success

        if change_available:
            indices, success = backtrack(word1_index + 1, word2_index + 1, False)
            if success:
                indices.append(word1_index)
                return indices, success

        i = word1_index
        while i < m and word1[i] != word2[word2_index]:
            i += 1

        if i < m:
            indices, success = backtrack(i + 1, word2_index + 1, change_available)
            if success:
                indices.append(i)
            return indices, success

        return [], False

    res_arr, res_success = backtrack(0, 0, True)
    return res_arr[::-1] if res_success else []


print(validSequence(word1="vbcca", word2="abc"))              # [0,1,2]
print(validSequence(word1="bacdc", word2="abc"))              # [1,2,4]
print(validSequence(word1="aaaaaa", word2="aaabc"))           # []
print(validSequence(word1="abc", word2="ab"))                 # [0,1]
print(validSequence(word1="kkkjkkjkkjjkjjkkjj", word2="jj"))  # [0,3]
