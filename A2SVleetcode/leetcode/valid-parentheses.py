class Solution:
    def isValid(self, s: str) -> bool:
        check=[]
        mapp={")":"(" , "]":"[" , "}":"{"}
        for i in s:
            if i in mapp.values():
                check.append(i)
            elif i in mapp.keys():
                  if not check or mapp[i]!=check.pop():
                      return False
        return len(check)==0
        