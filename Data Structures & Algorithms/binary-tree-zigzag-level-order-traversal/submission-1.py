from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
       
        # initrialize a queue 
        queue = deque([root])
        level = 1 # 1-indexed 
        while queue:
            temp_result = []
            for i in range(len(queue)):
                
               current_root =  queue.popleft()

               temp_result.append(current_root.val)
               if current_root.left:
                queue.append(current_root.left)
               if current_root.right:
                   queue.append(current_root.right)
            
            if level%2 ==0:
                temp_result.reverse()
            result.append(temp_result)
            
                
            level += 1 
        return result



               

