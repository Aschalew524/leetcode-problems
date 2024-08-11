# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.random_set = {}

    def insert(self, val: int) -> bool:
        if val not in self.random_set:
            self.random_set[val] = val
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            self.random_set.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.random_set))


