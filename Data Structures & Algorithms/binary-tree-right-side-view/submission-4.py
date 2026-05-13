# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        
        while queue:
            rightSide = None 
            qlen = len(queue)
            for i in range(qlen):
                curr = queue.popleft()
                if curr:
                    rightSide = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            if rightSide:
                res.append(rightSide.val)
        return res 

# after findiubg teh right we find the level number at which we hit none 
# we go left level many times 
# if l.rght:
# do the dssme recursively /as a func 
#IF l.rioght is nonr
# l.left


