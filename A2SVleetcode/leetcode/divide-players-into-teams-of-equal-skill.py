class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        numberofteam=len(skill)/2
        left=0
        right=len(skill)-1
        sumofchem=0
        totalskill=sum(skill)
        targetskill=totalskill//numberofteam
        while left < right:
            if skill[left]+skill[right]==targetskill:
                sumofchem+=skill[left]*skill[right]
                left+=1
                right-=1
            else:
                return -1
        return sumofchem

        