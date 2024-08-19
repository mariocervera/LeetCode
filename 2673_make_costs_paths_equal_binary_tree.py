def minIncrements(n, cost):
    def dfs_get_max_path_cost(node, path_cost):
        new_path_cost = path_cost + cost[node - 1]
        if node * 2 > n:
            return new_path_cost
        return max(
            dfs_get_max_path_cost(node * 2, new_path_cost),
            dfs_get_max_path_cost(node * 2 + 1, new_path_cost)
        )

    max_path_cost = dfs_get_max_path_cost(1, 0)

    def dfs_calc_slots(node, path_cost):
        new_path_cost = path_cost + cost[node - 1]
        if node * 2 > n:
            slots[node - 1] = max_path_cost - new_path_cost
        else:
            slots[node - 1] = min(
                dfs_calc_slots(node * 2, new_path_cost),
                dfs_calc_slots(node * 2 + 1, new_path_cost)
            )
        return slots[node - 1]

    slots = [0] * n
    dfs_calc_slots(1, 0)

    increments = 0

    def dfs_calc_increments(node, increments_on_path):
        nonlocal increments
        if node > n:
            return
        applied_increments = 0
        if slots[node-1] > 0:
            applied_increments = slots[node-1] - increments_on_path
        increments += applied_increments
        dfs_calc_increments(node * 2, increments_on_path + applied_increments)
        dfs_calc_increments(node * 2 + 1, increments_on_path + applied_increments)

    dfs_calc_increments(1, 0)

    return increments


print(minIncrements(n=7, cost=[1, 5, 2, 2, 3, 3, 1]))  # 6
print(minIncrements(n=3, cost=[5, 3, 3]))  # 0
