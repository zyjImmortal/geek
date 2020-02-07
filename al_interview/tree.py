class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root, p, q):
        '''给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。'''
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 对于一个节点，如果左右子树一个存在p，一个存在q节点，这个节点就是最近公共祖先
        if left:
            if right:
                return root
            else:
                return left
        else:
            return right