import time

def clear_string(s, i):
    n = len(s)
    if not (0 <= i < n) or not s:
        return s
    color, low, high = s[i], i, i
    while low >= 0 and s[low] == color:
        low -= 1
    while high < n and s[high] == color:
        high += 1
    low, high = low + 1, high - 1
    if s[low] != color or s[high] != color or high - low < 2:
        return s
    return clear_string(s[:low] + s[high + 1:], low - 1)


def findMinStep(board, hand):
    res = float("inf")
    dp = {}

    def backtrack(_board, _hand, i, steps):
        nonlocal res
        if (_board, _hand) in dp:
            return dp[(_board, _hand)]
        if not _board:
            res = min(res, steps)
            return
        if not _hand or i > len(_board):
            return
        backtrack(_board, _hand, i + 1, steps)
        for j in range(len(_hand)):
            new_board = _board[:i] + _hand[j] + _board[i:]
            new_board_cleared = clear_string(new_board, i)
            if new_board != new_board_cleared:
                backtrack(new_board_cleared, _hand[:j] + _hand[j + 1:], 0, steps + 1)
            else:
                backtrack(new_board, _hand[:j] + _hand[j + 1:], i + 1, steps + 1)
        dp[(_board, _hand)] = res

    backtrack(board, hand, 0, 0)
    return res if res != float("inf") else -1


start = time.time()

#print(findMinStep(board="RRYRRYYRRYYRYYRR", hand="YYYY"))  # 3  <- No me da resultado correcto.
print(findMinStep(board="RYYRRYYR", hand="YYYYY"))  # 5
print(findMinStep(board="WWRRBBWW", hand="WRBRW"))  # 2
print(findMinStep(board="G", hand="GGGGG"))  # 2
print(findMinStep(board="RRGGBBYYWWRRGGBB", hand="RGBYW"))  # -1
print(findMinStep(board="WRRBBW", hand="RB"))  # -1


end = time.time()
print(f"Execution time: {end - start}")