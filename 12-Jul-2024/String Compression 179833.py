# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars) :
        length, cnt = 0, 1
        chars.append("##")
        
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                cnt += 1
            else:
                chars[length] = chars[i-1]
                length += 1
                if cnt > 1:
                    for ch in str(cnt):
                        chars[length] = ch
                        length += 1
                cnt = 1
        
        return length