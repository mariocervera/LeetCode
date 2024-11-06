def splitWordsBySeparator(words, separator):
    res = []
    for word in words:
        for w in word.split(separator):
            if len(w) > 0:
                res.append(w)
    return res


print(splitWordsBySeparator(words=["a.b.c", "d.e", "f"], separator="."))  # ["a","b","c","d","e","f"]
print(splitWordsBySeparator(words=["$easy$", "$problem$"], separator="$"))  # ["easy","problem"]
print(splitWordsBySeparator(words=["|||"], separator="|"))  # []
