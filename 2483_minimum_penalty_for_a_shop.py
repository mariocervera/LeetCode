
def bestClosingTime(customers):
    n_count, y_count = 0, sum(1 if c == "Y" else 0 for c in customers)
    min_penalty, res = float("inf"), 0
    for i in range(len(customers)):
        penalty = n_count + y_count
        if penalty < min_penalty:
            min_penalty = penalty
            res = i
        if customers[i] == "Y":
            y_count -= 1
        else:
            n_count += 1
    return res if n_count >= min_penalty else len(customers)


print(bestClosingTime("YYNY"))  # 2
print(bestClosingTime("NNNNN"))  # 0
print(bestClosingTime("YYYY"))  # 4
