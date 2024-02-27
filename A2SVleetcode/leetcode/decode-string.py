class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                s = ''
                while stack[-1] != '[':
                    s = stack[-1] + s
                    stack.pop(-1)
                stack.pop(-1)
                nums = ''
                while stack and stack[-1].isdigit():
                    nums= stack[-1] + nums
                    stack.pop(-1)
                s *= int(nums)
                stack.append(s)
        return ''.join(stack)
            