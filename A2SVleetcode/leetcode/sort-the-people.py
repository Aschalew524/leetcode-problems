class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        l = zip(names, heights)
        l = sorted(l, key=lambda x: x[1], reverse=True)
        return [i[0] for i in l]