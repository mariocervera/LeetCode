
def compareVersion(version1, version2):
    arr_1, arr_2 = list(map(int, version1.split("."))), list(map(int, version2.split(".")))

    if len(arr_1) < len(arr_2):
        arr_1.extend([0] * (len(arr_2) - len(arr_1)))
    elif len(arr_1) > len(arr_2):
        arr_2.extend([0] * (len(arr_1) - len(arr_2)))

    if arr_1 < arr_2:
        return -1
    elif arr_1 > arr_2:
        return 1
    return 0


print(compareVersion("1.01", "1.001"))  # 0
print(compareVersion("1.0", "1.0.0"))  # 0
print(compareVersion("1.0.0.0.0.000", "1.0.0"))  # 0

print(compareVersion("0.1", "1.1"))  # -1

print(compareVersion("1.2", "1.1"))  # 1
print(compareVersion("1.0.1", "1"))  # 1
