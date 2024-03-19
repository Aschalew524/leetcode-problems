class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half, right_half):
            l = 0
            r = 0
            merged = []
            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    merged.append(left_half[l])
                    l += 1
                else:
                    merged.append(right_half[r])
                    r += 1
            while l < len(left_half):
                merged.append(left_half[l])
                l += 1
            while r < len(right_half):
                merged.append(right_half[r])
                r += 1
            return merged
        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            return merge(left_half, right_half)
        
        return mergeSort(0, len(nums) - 1, nums)
