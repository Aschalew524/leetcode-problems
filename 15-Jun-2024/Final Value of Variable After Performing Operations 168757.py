# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for s in operations:
            if s=="--X" or s== "X--":
                x-=1
            else:
                x+=1
        return x

        """
        :type operations: List[str]
        :rtype: int
        """
        