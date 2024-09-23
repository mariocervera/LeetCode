
def reportSpam(message, bannedWords):
    bannedWords = set(bannedWords)
    counter = 0
    for word in message:
        if word in bannedWords:
            counter += 1
            if counter == 2:
                return True
    return False


print(reportSpam(message=["hello", "world", "leetcode"],
                 bannedWords=["world", "hello"]))  # True
print(reportSpam(message=["hello", "programming", "fun"],
                 bannedWords=["world", "programming", "leetcode"]))  # False
