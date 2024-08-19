
'''
def convert(s, numRows):
    if numRows == 1:
        return s
    res = []
    for row in range(numRows):
        increasing_step, decreasing_step, fixed_step = row * 2, (numRows - row - 1) * 2, (numRows - 1) * 2
        i, b = row, True
        while i < len(s):
            res.append(s[i])
            if row == 0 or row == numRows - 1:
                i += fixed_step
            else:
                i += (decreasing_step if b else increasing_step)
            b = not b
    return "".join(res)
'''

def convert(s, numRows):
    if numRows == 1:
        return s
    rows = [''] * numRows
    index, direction = 0, -1
    for c in s:
        rows[index] += c
        if index == 0 or index == numRows-1:
            direction *= -1
        index += direction
    return "".join(rows)


print(convert(s="PAYPALISHIRING", numRows=3))  # "PAHNAPLSIIGYIR"
print(convert(s="PAYPALISHIRING", numRows=4))  # "PINALSIGYAHRPI"
print(convert(s="A", numRows=1))  # "A"
