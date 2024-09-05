from collections import Counter

def bestHand(ranks, suits):
    suits_counter = Counter(suits)
    ranks_counter, max_rank_counter = {}, 0
    for rank in ranks:
        ranks_counter[rank] = ranks_counter.get(rank, 0) + 1
        max_rank_counter = max(max_rank_counter, ranks_counter[rank])
    if len(suits_counter) == 1:
        return "Flush"
    elif max_rank_counter >= 3:
        return "Three of a Kind"
    elif max_rank_counter == 2:
        return "Pair"
    return "High Card"


print(bestHand(ranks=[13, 2, 3, 1, 9],
               suits=["a", "a", "a", "a", "a"]))  # "Flush"

print(bestHand(ranks=[4, 4, 2, 4, 4],
               suits=["d", "a", "a", "b", "c"]))  # "Three of a Kind"

print(bestHand(ranks=[10, 10, 2, 12, 9],
               suits=["a", "b", "c", "a", "d"]))  # "Pair"
