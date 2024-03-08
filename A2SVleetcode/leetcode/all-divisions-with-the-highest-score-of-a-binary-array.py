class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_1 = 0
        for i in nums:
            if i == 1:
                 count_1 += 1
        
        cnt_0, max_d = 0, count_1
        d = collections.defaultdict(list)
        d[count_1].append(0)
        for i, v in enumerate(nums):
            cnt_0 += int(v == 0)
            count_1 -= int(v == 1)
            d[cnt_0 + count_1].append(i + 1)
            max_d = max(max_d, cnt_0 + count_1)
        return d[max_d]