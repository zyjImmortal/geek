# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """树的某条路径上的节点之和等于sum"""
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def maxDepth(self, root):
        """树的最大深度"""
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left) + self.minDepth(root.right))