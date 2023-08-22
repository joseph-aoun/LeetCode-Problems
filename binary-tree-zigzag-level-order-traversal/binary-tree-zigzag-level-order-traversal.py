# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def dfs(root, h = 1):
            if not root: return
            if h > len(levels):
                levels.append([])
            levels[h-1].append(root.val)
            dfs(root.left, h+1)
            dfs(root.right, h+1)
        dfs(root)
        for i in range(len(levels)):
            if i&1: levels[i].reverse()
        return levels