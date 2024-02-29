class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = blocks[:k].count('W')
        num_of_operations = w

        for right in range(k, len(blocks)):
            if blocks[right - k] == 'W':
                w -= 1

            if blocks[right] == 'W':
                w += 1

            num_of_operations = min(num_of_operations, w)

        return num_of_operations