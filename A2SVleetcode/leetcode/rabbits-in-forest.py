class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = 0
        colors= Counter(answers)
        for rabbit,color in colors.items():
            number = math.ceil(color/(rabbit+1))
            rabbits = rabbits + (number * (rabbit+1))
        return rabbits