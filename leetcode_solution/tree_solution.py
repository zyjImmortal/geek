# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode):
        '''
        给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
        s 的一个子树包括 s 的一个节点和这个节点的所有子孙。
        s 也可以看做它自身的一棵子树
        :param s:
        :param t:
        :return:
        '''
        pass

    def diameterOfBinaryTree(self, root: TreeNode):
        '''
        给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
        示例 :
        给定二叉树

                  1
                 / \
                2   3
               / \
              4   5
        返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

        注意：两结点之间的路径长度是以它们之间边的数目表示
        :param root:
        :return:
        '''
        pass

    def buildTree(self, inorder, postorder):
        """
        根据一棵树的中序遍历与后序遍历构造二叉树
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        pass
    
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 