
def is_arithmetic(arr):
    if len(arr) < 2:
        return False
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True

def checkArithmeticSubarrays(nums, l, r):
    return [is_arithmetic(nums[l[i]:r[i]+1]) for i in range(len(l))]



# [true,false,true]
print(checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7],
                               l=[0, 0, 2],
                               r=[2, 3, 5]))

# [false,true,false,false,true,true]
print(checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
                               l=[0, 1, 6, 4, 8, 7],
                               r=[4, 4, 9, 7, 9, 10]))
