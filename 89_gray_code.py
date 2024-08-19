
def grayCode(n):
    if n == 1:
        return [0, 1]
    arr_low = [num << 1 for num in grayCode(n-1)]
    arr_high = [num | 1 for num in arr_low[::-1]]
    return arr_low + arr_high


print(grayCode(1))  # [0,1]
print(grayCode(2))  # [0,1,3,2]
print(grayCode(3))  # [0, 4, 6, 2, 3, 7, 5, 1]
