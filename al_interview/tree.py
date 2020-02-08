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


    '''二叉树的遍历
    前中后，根究root的位置，
    '''

    '''分治算法代码模板'''

    def divid_conquer(self, problem, params1, params2):
        # 递归终止条件
        if problem is None:
            return

        # 处理数据
        # data = prepare_data(problem)
        # sub_problems = split_problem(problem)

        # sub_result1 = self.divid_conquer(sub_problems[0])
        # sub_result2 = self.divid_conquer(sub_problems[1])
        # sub_result3 = self.divid_conquer(sub_problems[2])
        #
        # # 手机处理结果，并返回
        # result = proccess_result(sub_result1,sub_result2 ....)


    '''x 的n次方'''
    def pow(self, x, n):
        return pow(x, n)