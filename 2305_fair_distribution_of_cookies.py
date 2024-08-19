

def distributeCookies(cookies, k):
    n, res = len(cookies), float("inf")

    def backtrack(solution, i):
        nonlocal res
        if i == n:
            res = min(res, max(solution))
            return
        for num in range(k):
            solution[num] += cookies[i]
            if solution[num] > res:
                solution[num] -= cookies[i]
                continue
            backtrack(solution, i+1)
            solution[num] -= cookies[i]

    backtrack([0] * k, 0)

    return res


print(distributeCookies([8, 15, 10, 20, 8], 2))  # 31
print(distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))  # 7
