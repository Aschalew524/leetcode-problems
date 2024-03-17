class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        peak = max(arr)
        if peak == arr[len(arr) - 1] or peak == arr[0]:
            return False
        max_ = False
        for i in range(len(arr) - 1):
            
            if arr[i] ==peak:
                max_ = True
            if max_ and arr[i] <= arr[i + 1]:
                return False
            elif not max_ and arr[i] >= arr[i + 1]:
                return False
        return True