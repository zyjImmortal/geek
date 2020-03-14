from node import Node


class BinarySearchTree:

    def __init__(self):
        self.tree = None
        self._result = []

    def find(self, data):
        p = self.tree
        while p:
            if data < p.data:
                p = p.left
            elif data > p.data:
                p = p.right
            else:
                return p.data
        return Node

    def insert(self, data: int):
        if self.tree is None:
            self.tree = Node(data)
        p = self.tree
        while p:
            if data > p.data:
                if p.right is None:
                    p.right = Node(data)
                    return self
                p = p.right
            else:
                if p.left is None:
                    p.left = Node(data)
                    return self
                p = p.left

    def delete(self, data):
        '''删除操作'''
        c = self.tree
        p = None
        # 在树中查找值等于data的节点，循环停止要么找到要么没找到
        #
        while c and c.data != data:
            p = c
            if data > c.data:
                c = c.right
            else:
                c = c.left
        # 如果没找到直接返回
        if c is None:
            return
        if c.left and c.right:
            minc = c.right
            while minc.left:
                minp = minc
                minc = minc.left
            c.data = minc.data
            c = minc
            p = minp

        if c.left:
            child = c.left
        elif c.right:
            child = c.right
        else:
            child = None

        if p.left == data:
            p.left = child
        elif p.right == data:
            p.right = child

        # 进行删除操作
        if not p:
            self.tree = child
        elif p.left == c:
            p.left = child
        else:
            p.right = child



    def _pre_order(self, tree):
        p = tree
        if p is None:
            return
        self._result.append(str(p.data))
        self._pre_order(p.left)
        self._pre_order(p.right)
    def __str__(self):
        ''''''
        self._pre_order(self.tree)
        return '->'.join(self._result)

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(44).insert(55).insert(22).insert(11).insert(88)
    print(tree)
