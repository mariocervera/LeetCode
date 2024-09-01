
class Enemy:
    def __init__(self, index, damage, hits):
        self.index = index
        self.damage = damage
        self.hits = hits

    def __lt__(self, other):
        return self.damage * other.hits >= other.damage * self.hits


def minDamage(power, damage, health):
    res, total_damage, n = 0, 0, len(damage)
    enemies = [None] * n
    for i in range(n):
        total_damage += damage[i]
        enemies[i] = Enemy(i, damage[i], health[i] // power + (1 if health[i] % power != 0 else 0))
    enemies.sort()
    for enemy in enemies:
        res += (total_damage * enemy.hits)
        total_damage -= enemy.damage
    return res


print(minDamage(power=4,
                damage=[1, 2, 3, 4],
                health=[4, 5, 6, 8]))  # 39

print(minDamage(power=1,
                damage=[1, 1, 1, 1],
                health=[1, 2, 3, 4]))  # 20

print(minDamage(power=8,
                damage=[40],
                health=[59]))  # 320
