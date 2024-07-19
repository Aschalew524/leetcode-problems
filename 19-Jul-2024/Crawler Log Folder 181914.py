# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        op = 0
        for log in logs:
            if log == "../":
                op -= 1 if op > 0 else 0
            elif log == "./":
                op += 0
            else:
                op += 1
        return op