
def to_binary_string(str_number):
    return bin(int(str_number))[2:]

def convertDateToBinary(date):
    return "-".join([to_binary_string(num) for num in date.split("-")])


print(convertDateToBinary("2080-02-29"))  # "100000100000-10-11101"
print(convertDateToBinary("1900-01-01"))  # "11101101100-1-1"
