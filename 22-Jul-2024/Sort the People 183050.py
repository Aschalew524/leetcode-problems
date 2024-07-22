# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        check = zip(names, heights)
        check = sorted(check, key=lambda x: x[1], reverse=True)
        return [i[0] for i in check]