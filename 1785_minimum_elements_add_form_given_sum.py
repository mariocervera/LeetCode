
def minElements(nums, limit, goal):
    diff = abs(sum(nums) - goal)
    div = diff // limit
    remainder = diff % limit
    return div if remainder == 0 else div+1


print(minElements(nums=[1, -1, 1], limit=3, goal=-4))  # 2
print(minElements(nums=[1, -10, 9, 1], limit=100, goal=0))  # 1
print(minElements(nums=[2, 2, 2, 5, 1, -2], limit=5, goal=126614243))  # 25322847
