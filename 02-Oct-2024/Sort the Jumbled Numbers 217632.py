# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        lis=[]
        for i in nums:
            str1=""
            for j in range(len(str(i))):
                str1+=str(mapping[int(str(i)[j])])
            lis.append(int(str1))
        dicts=defaultdict(list)
        
        for i in range(len(lis)):
            dicts[lis[i]].append(nums[i])
        ans=[]
        for i in sorted(set(lis)):
            ans+=dicts[i]

        
        return(ans)


        