class Solution:
    def isAlphanumeric(self, char):
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while right > left and not self.isAlphanumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
            
        return True


