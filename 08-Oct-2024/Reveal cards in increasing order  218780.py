# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ans = [deck[0]]
        l = 1  
        while l < len(deck):
            ans.insert(0, ans.pop())
            ans.insert(0, deck[l])
            l += 1
        return ans