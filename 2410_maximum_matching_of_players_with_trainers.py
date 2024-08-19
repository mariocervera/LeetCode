
def matchPlayersAndTrainers(players, trainers):
    players.sort()
    trainers.sort()
    i, n = 0, len(players)
    for trainer in trainers:
        if players[i] <= trainer:
            i += 1
        if i == n:
            break
    return i


print(matchPlayersAndTrainers(players=[4, 7, 9], trainers=[8, 2, 5, 8]))  # 2
print(matchPlayersAndTrainers(players=[1, 1, 1], trainers=[10]))  # 1
print(matchPlayersAndTrainers(players=[4,2], trainers=[4,4,3]))  # 1