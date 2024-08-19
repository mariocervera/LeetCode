
def get_initial_number(size):
    res = 0
    for digit in range(1, size+1):
        res = res * 10 + digit
    return res


def get_sequentials_of_size(size):
    num = get_initial_number(size)
    res = [num]
    for digit in range(size+1, 10):
        num = num % (10 ** (size-1)) * 10 + digit
        res.append(num)
    return res


def sequentialDigits(low, high):
    res = []
    for size_i in range(1, 10):
        for seq in get_sequentials_of_size(size_i):
            if low <= seq <= high:
                res.append(seq)
            if seq > high:
                return res
    return res



print(sequentialDigits(low=100, high=300))  # [123,234]
print(sequentialDigits(low=1000, high=13000))  # [1234,2345,3456,4567,5678,6789,12345]
print(sequentialDigits(low=10, high=1000000000))

