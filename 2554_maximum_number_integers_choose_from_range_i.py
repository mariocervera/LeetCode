
def maxCount(banned, n, maxSum):
    banned_numbers = set(banned)
    current_sum, res = 0, 0
    for number in range(1, n+1):
        if number in banned_numbers:
            continue
        if current_sum + number <= maxSum:
            current_sum += number
            res += 1
    return res



print(maxCount(banned=[1, 6, 5], n=5, maxSum=6))  # 2
print(maxCount(banned=[1, 2, 3, 4, 5, 6, 7], n=8, maxSum=1))  # 0
print(maxCount(banned=[11], n=7, maxSum=50))  # 7
