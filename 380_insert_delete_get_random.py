import random

class RandomizedSet:

    def __init__(self):
        self.ht = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.ht:
            return False
        i = len(self.arr)
        self.arr.append(val)
        self.ht[val] = i
        return True

    def remove(self, val: int) -> bool:
        if val not in self.ht:
            return False
        i = self.ht[val]
        val_to_move = self.arr[-1]
        self.ht[val_to_move] = i
        self.arr[i] = val_to_move
        self.arr.pop()
        self.ht.pop(val)
        return True

    def getRandom(self) -> int:
        random_i = random.randint(0, len(self.arr)-1)
        return self.arr[random_i]


obj = RandomizedSet()
print(obj.remove(0))
print(obj.remove(0))
print(obj.insert(0))
print(obj.getRandom())
print(obj.remove(0))
print(obj.insert(0))
