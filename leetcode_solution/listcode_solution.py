class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseListNode(self):
        pass

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点
        两次遍历
        :param head:
        :param n:
        :return:
        """
        if head == None:
            return head
        size = 0
        temp = head
        while temp != None:
            size += 1
            temp = temp.next
        a = size - n
        temp = head
        while a > 0:
            a -= 1
            temp = temp.next
        node = temp.next.next
        head.next = node
        return head

    def removeNthFromEndV2(self, head: ListNode, n: int) -> ListNode:
        """
        快慢指针，快指针先走n步，然后两个指针一起走知道快指针到尾部
        :param head:
        :param n:
        :return:
        """
        temp = ListNode()
        temp.next = head
        first = temp
        second = temp
        # 快指针先走n步
        for i in range(0, n + 1):
            first = first.next
        # 两个指针一起走，走完剩余length-n步，这个时候慢指针刚好走到倒数n个节点的前一个节点
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return temp.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字
        :param head:
        :return:
        """
        if head == None or head.next == None:
            return head
        dumpy = ListNode(-1)
        dumpy.next = head
        cur = dumpy.next
        pre = dumpy
        while cur.next != None:
            if cur.val != cur.next.val:
                if pre.next.val == cur.val:
                    pre = cur
                else:
                    pre.next = cur.next
            cur = cur.next
        return dumpy.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(4)
node.next.next.next.next.next = ListNode(4)
node.next.next.next.next.next.next = ListNode(5)

import util
util.print_list_node(node)
solution = Solution()
solution.deleteDuplicates(node)
