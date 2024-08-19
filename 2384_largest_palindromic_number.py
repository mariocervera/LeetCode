from collections import Counter
import heapq

def largestPalindromic(num):
    counter = Counter(num)
    if len(counter) == 1 and "0" in counter:
        return "0"
    pq = []
    max_single = None
    for digit, frequency in counter.items():
        digit = int(digit)
        if frequency % 2 == 0:
            heapq.heappush(pq, (digit * -1, frequency // 2))
            continue
        if frequency > 1:
            heapq.heappush(pq, (digit * -1, (frequency - 1) // 2))
        if not max_single or digit > max_single:
            max_single = digit
    res = []
    if pq and pq[0][0] == 0:
        pq.clear()
    while pq:
        item = heapq.heappop(pq)
        res.extend([str(abs(item[0]))] * item[1])
    res_str = "".join(res)

    return res_str + (str(max_single) if max_single is not None else "") + res_str[::-1]


print(largestPalindromic("444947137"))  # "7449447"
print(largestPalindromic("00009"))  # "9"
print(largestPalindromic("6006"))  # "6006"
print(largestPalindromic("00000"))  # "0"
print(largestPalindromic("00011"))  # "10001"

