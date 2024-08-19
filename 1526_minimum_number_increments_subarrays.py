
def minNumberOperations(target):
    n = len(target)
    if n == 1:
        return target[0]

    stack = [0]
    next_lower_to_left = [-1] * n
    for i in range(1, n):
        while stack and target[i] <= target[stack[-1]]:
            stack.pop()
        next_lower_to_left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack = [n-1]
    next_lower_to_right = [n] * n
    for i in range(n-2, -1, -1):
        while stack and target[i] <= target[stack[-1]]:
            stack.pop()
        next_lower_to_right[i] = stack[-1] if stack else n
        stack.append(i)

    sorted_targets = sorted([(t, i) for i, t in enumerate(target)])
    i, filtered_sorted_targets = 0, []
    for j in range(1, n):
        i_value, i_index = sorted_targets[i][0], sorted_targets[i][1]
        j_value, j_index = sorted_targets[j][0], sorted_targets[j][1]
        if i_value != j_value or (j_index <= next_lower_to_left[i_index] or j_index >= next_lower_to_right[i_index]):
            filtered_sorted_targets.append(sorted_targets[i])
            i = j
    filtered_sorted_targets.append(sorted_targets[i])

    operations = 0
    for t, i in filtered_sorted_targets:
        limit_left, limit_right = 0, 0
        if next_lower_to_left[i] != -1:
            limit_left = target[next_lower_to_left[i]]
        if next_lower_to_right[i] != n:
            limit_right = target[next_lower_to_right[i]]
        operations += (target[i] - max(limit_left, limit_right))
    return operations


print(minNumberOperations([1, 2, 3, 2, 1]))  # 3
print(minNumberOperations([3, 1, 1, 2]))  # 4
print(minNumberOperations([3, 1, 5, 4, 2]))  # 7
