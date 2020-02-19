import collections


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

    '''层序遍历'''

    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = collections.deque()  # 队列存储每一层所有的节点
        queue.append(root)
        # while循环控制一层一层往下走，内层for循环控制读取每一层数据
        while queue:
            current_level = []
            size = len(queue)
            # 遍历当前层所有节点的值，然后把子节点存入队列
            for _ in range(size):
                node = queue.popleft()
                current_level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

    def levelOrderV2(self, root):
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node:
            return
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(node.val)
        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.levelOrder())
