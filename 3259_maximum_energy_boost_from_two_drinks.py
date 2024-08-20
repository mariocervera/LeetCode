
def maxEnergyBoost(energyDrinkA, energyDrinkB):
    n = len(energyDrinkA)
    prev_prev_a, prev_prev_b = energyDrinkA[0], energyDrinkB[0]
    prev_a, prev_b = prev_prev_a + energyDrinkA[1], prev_prev_b + energyDrinkB[1]
    for i in range(2, n):
        current_a = max(prev_a + energyDrinkA[i], prev_prev_b + energyDrinkA[i])
        current_b = max(prev_b + energyDrinkB[i], prev_prev_a + energyDrinkB[i])
        prev_prev_a, prev_prev_b = prev_a, prev_b
        prev_a, prev_b = current_a, current_b
    return max(current_a, current_b)


print(maxEnergyBoost(energyDrinkA=[1, 3, 1], energyDrinkB=[3, 1, 1]))  # 5
print(maxEnergyBoost(energyDrinkA=[4, 1, 1], energyDrinkB=[1, 1, 3]))  # 7
