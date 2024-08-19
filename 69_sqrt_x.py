
def binary_search(low, high, x):
    while low < high:
        mid = (low+high)//2
        square = mid * mid
        next_square = (mid+1)*(mid+1)

        if square <= x < next_square:
            return mid
        elif square > x:
            high = mid - 1
        else:
            low = mid + 1
    return low

def mySqrt(x):
    return binary_search(0, x, x)


print(mySqrt(4))   # 2
print(mySqrt(8))   # 2
print(mySqrt(9))   # 3
print(mySqrt(11))  # 3
print(mySqrt(16))  # 4
