# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 3 -> [ l ]
        # 9 -> [l l ]
        # get teh parents and also the level of parents of both p and q 
        # choose the common parents 
        # from that we return the lowest level parent 
        # we cabn take the fact that the tree is a BST to our advnatgage and do this 
        # by comparing teh values
        curr = root
        while curr: 
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right 
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            else:
                return curr
        return None 