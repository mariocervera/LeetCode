
class NestedInteger:
   def isInteger(self) -> bool:
       return False

   def getInteger(self) -> int:
       return 0

   def getList(self) -> [NestedInteger]:
       return []

class NestedIterator:
    def __init__(self, nestedList):
        self.flattened_list = []

        def __flatten(obj):
            if not obj:
                return
            if obj.isInteger():
                self.flattened_list.append(obj.getInteger())
            else:
                _list = obj.getList()
                for nested_obj in _list:
                    __flatten(nested_obj)

        for l in nestedList:
            __flatten(l)

        self.index = 0
        self.length = len(self.flattened_list)

    def next(self):
        num = self.flattened_list[self.index]
        self.index += 1
        return num

    def hasNext(self):
        return self.index < self.length



ni = NestedIterator([1, 2, 3, [4, 5, 6, [7, 8, 9]]])
while ni.hasNext():
    print(str(ni.next()) + " ")
