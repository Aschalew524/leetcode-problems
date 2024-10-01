# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counter = defaultdict(int)
        winners = set()
        loosers = []

        for winner, loser in matches:
            winners.add(winner)
            counter[loser] += 1

        for loser, cnt in counter.items():
            if loser in winners:
                winners.remove(loser)
            if cnt == 1:
                loosers.append(loser)

        return [sorted(list(winners)), sorted(loosers)]