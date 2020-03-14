from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:


    def helper(self, root, res):
        ''''''
        if root:
            if root.left:
                self.helper(root.left, res)
            res.append(root.val)
            if root.right:
                self.helper(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        给定一个二叉树，返回它的中序 遍历。
        示例:
        输入: [1,null,2,3]
           1
            \
             2
            /
           3
        输出: [1,3,2]
        进阶: 递归算法很简单，你可以通过迭代算法完成吗？
        :param root:
        :return:
        '''
        res = []
        self.helper(root, res)
        return res
