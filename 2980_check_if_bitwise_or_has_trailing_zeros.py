
def hasTrailingZeros(nums):
    even_num_counter = 0
    for num in nums:
        if num % 2 == 0:
            even_num_counter += 1
    return even_num_counter > 1


print(hasTrailingZeros([1, 2, 3, 4, 5]))  # True
print(hasTrailingZeros([2, 4, 8, 16]))  # True
print(hasTrailingZeros([1, 3, 5, 7, 9]))  # False
