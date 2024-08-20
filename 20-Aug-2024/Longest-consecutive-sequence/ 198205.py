# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count, count = 0, 1
        num_set = set(nums)

        while num_set:
            num = num_set.pop()
            temp = num

            while num + 1 in num_set:
                count += 1
                num_set.remove(num + 1)
                num += 1

            num = temp

            while num - 1 in num_set:
                count += 1
                num_set.remove(num - 1)
                num -= 1

            max_count = max(max_count, count)

            count = 1

        return max_count