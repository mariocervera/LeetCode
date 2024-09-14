
def stableMountains(height, threshold):
    res = []
    for i in range(1, len(height)):
        if height[i-1] > threshold:
            res.append(i)
    return res


print(stableMountains(height=[1, 2, 3, 4, 5], threshold=2))  # [3,4]
print(stableMountains(height=[10, 1, 10, 1, 10], threshold=3))  # [1,3]
print(stableMountains(height=[10, 1, 10, 1, 10], threshold=10))  # []
