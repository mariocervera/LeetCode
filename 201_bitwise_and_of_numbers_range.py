
def rangeBitwiseAnd(left, right):
    bits_diff = (right-left).bit_length()
    mask = ~((1 << bits_diff) - 1) & 0xffffffff
    return (left & mask) & (right & mask)

def rangeBitwiseAnd(left, right):
    while right > left:
        right &= right - 1
    return left & right

print(rangeBitwiseAnd(left=24, right=31))  # 24
print(rangeBitwiseAnd(left=5, right=7))  # 4
print(rangeBitwiseAnd(left=0, right=0))  # 0
print(rangeBitwiseAnd(left=1, right=2147483647))  # 0

# x = 8
# y = 11
#
# print(f"x: {bin(x)}")
# print(f"y: {bin(y)}")
# print(f"y-x ({y-x}): {bin(y-x)}")
#
# print(f"Result: {rangeBitwiseAnd(left=x, right=y)}")



