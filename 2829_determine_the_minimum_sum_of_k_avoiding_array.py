def minimumSum(n, k):
    left_len = min(n, k//2)
    right_len = n - left_len
    sum_left = (left_len * (left_len + 1)) // 2
    sum_right = ((k + k + right_len - 1) * right_len) // 2
    return sum_left + sum_right


print(minimumSum(n=5, k=4))  # 18
print(minimumSum(n=2, k=6))  # 3
