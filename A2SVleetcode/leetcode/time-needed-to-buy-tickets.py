class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque([i for i in range(len(tickets))])
        
        count = 0
        while que:
            for i in range(len(que)):
                x = que.popleft()
                if tickets[x] >= 1:
                    tickets[x] -= 1
                    count += 1
                    que.append(x)
                
                if tickets[k] == 0:
                    return count

        return count