
def sortArrayByParity(nums):
    n = len(nums)
    res = [0] * n
    i, j = 0, -1
    for num in nums:
        if num % 2 == 0:
            res[i] = num
            i += 1
        else:
            res[j] = num
            j -= 1
    return res


print(sortArrayByParity([3, 1, 2, 4]))  # [2,4,1,3]
print(sortArrayByParity([2, 1, 5, 9, 3, 6]))  # [2,6,3,9,5,1]
print(sortArrayByParity([0]))  # [0]
