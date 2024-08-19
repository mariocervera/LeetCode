
# def minOperations(n):
#     ops = 0 if n % 2 else 1
#     x = ops + 2
#     iterations = n//2 if n % 2 else n//2 - 1
#     for _ in range(iterations):
#         ops += x
#         x += 2
#     return ops

def minOperations(n):
    half = n//2
    if n % 2 != 0:
        return half * (half+1)
    return half ** 2


print(minOperations(3))  # 2
print(minOperations(6))  # 9
