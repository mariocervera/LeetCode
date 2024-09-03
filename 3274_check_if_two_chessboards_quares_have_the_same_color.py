def checkTwoChessboards(coordinate1, coordinate2):
    x1, y1 = (ord(coordinate1[0]) - ord('a') + 1), int(coordinate1[1])
    x2, y2 = (ord(coordinate2[0]) - ord('a') + 1), int(coordinate2[1])
    return (x1 % 2 == x2 % 2 and y1 % 2 == y2 % 2) or \
        (x1 % 2 != x2 % 2 and y1 % 2 != y2 % 2)


print(checkTwoChessboards(coordinate1="a1", coordinate2="c3"))  # True
print(checkTwoChessboards(coordinate1="a1", coordinate2="h3"))  # False
print(checkTwoChessboards(coordinate1="b6", coordinate2="d4"))  # True
print(checkTwoChessboards(coordinate1="b6", coordinate2="d5"))  # False
print(checkTwoChessboards(coordinate1="c2", coordinate2="g4"))  # True
print(checkTwoChessboards(coordinate1="h7", coordinate2="c8"))  # True
