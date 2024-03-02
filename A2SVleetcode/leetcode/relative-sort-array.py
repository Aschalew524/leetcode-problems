class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sorted_ = []

        for i in arr2:
            while i in arr1:
                
                sorted_  .append(i)
                arr1.remove(i)

        return(sorted_ + sorted(arr1))