# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = collections.Counter(word)
        count = sorted(list(count.items()), key= lambda x:x[1], reverse= True)
        ans = 0
        for i in range(len(count)):
            ans +=  (i //8 + 1) * count[i][1]
        return ans 