# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        def ok(p, q):
            if not p or not q:
                return not (p or q)
            return p.val == q.val and ok(p.left, q.left) and ok(p.right, q.right)
        return ok(p, q)