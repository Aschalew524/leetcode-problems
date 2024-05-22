# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=deque([0])
        possible=set([0])
        while queue:
            cur=queue.popleft()
            for key in rooms[cur]:
                if key not in possible:
                    possible.add(key)
                    queue.append(key)
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] not in possible:
                    return False
        return True
        
       

    
       
        
    
    

            
        

       
        
            

        