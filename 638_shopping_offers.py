
def is_applicable(offer, needs):
    for i in range(len(needs)):
        if offer[i] > needs[i]:
            return False
    return True


def take_offer(offer, needs):
    for i in range(len(needs)):
        needs[i] -= offer[i]
    return needs


def undo_offer(offer, needs):
    for i in range(len(needs)):
        needs[i] += offer[i]
    return needs


def shoppingOffers(price, special, needs):

    dp = {}

    def backtrack(needs_left):
        t = tuple(needs_left)
        if t in dp:
            return dp[t]

        if sum(needs_left) == 0:
            return 0

        res = float("inf")
        for offer in special:
            if is_applicable(offer, needs_left):
                take_offer(offer, needs_left)
                res = min(res, offer[-1] + backtrack(needs_left))
                undo_offer(offer, needs_left)

        for i in range(len(needs_left)):
            if needs_left[i] > 0:
                needs_ith_item = needs_left[i]
                needs_left[i] = 0
                res = min(res, price[i] * needs_ith_item + backtrack(needs_left))
                needs_left[i] = needs_ith_item

        dp[t] = res
        return res

    return backtrack(needs)


print(shoppingOffers(price=[2, 5],
                     special=[[3, 0, 5],
                              [1, 2, 10]],
                     needs=[3, 2]))  # 14

print(shoppingOffers(price=[2, 3, 4],
                     special=[[1, 1, 0, 4],
                              [2, 2, 1, 9]],
                     needs=[1, 2, 1]))  # 11
