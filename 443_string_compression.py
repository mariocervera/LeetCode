
def compress(chars):
    i, j, n = 0, 0, len(chars)
    while j < n:
        start_index, start_char = j, chars[j]
        while j < n and chars[j] == start_char:
            j += 1
        chars[i] = start_char
        i += 1
        streak_len = j - start_index
        if streak_len > 1:
            s_streak_len = str(streak_len)
            for c in s_streak_len:
                chars[i] = c
                i += 1
    return i



arr0 = ["a","a","a","b","b","a","a"]
print(compress(arr0))  # 4
print(arr0)  # First 4 characters of the input array: ["a","3","b","2","a","2"]]

arr1 = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(arr1))  # 6
print(arr1)  # First 6 characters of the input array: ["a","2","b","2","c","3"]

arr2 = ["a"]
print(compress(arr2))  # 1
print(arr2)  # First 1 character of the input array: ["a"]

arr3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compress(arr3))  # 4
print(arr3)  # First 4 characters of the input array: ["a","b","1","2"]
