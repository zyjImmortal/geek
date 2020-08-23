from leetcode_solution.listcode_solution import ListNode


class Solution:
    '''
    链表问题类型：
    链表数字求和
    '''

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        给出两个 非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
        并且它们的每个节点只能存储 一位 数字。
        如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和
        :param l1:
        :param l2:
        :return:
        '''
        p1, p2 = l1, l2
        result = ListNode(0)
        cur = result
        carry = 0
        while p1 != None or p2 != None:
            val1 = p1.val if p1 != None else 0
            val2 = p2.val if p2 != None else 0
            val = val1 + val2 + carry
            carry = val // 10  # 整数是进位，和下一个节点的值一起求和
            result.next = ListNode(val % 10)  # 余数保留在当前位
            cur = cur.next
            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return result.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''编写一个程序，找到两个单链表相交的起始节点'''

        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数'''
        if not head or not head.next:
            return head
        start = pre = head
        cur = pre.next
        while k > 0:
            while cur.next:
                pre = pre.next
                cur = cur.next
            pre.next = None
            cur.next = start
            pre = start = cur
            cur = cur.next
            k -= 1
        return head

    def rotateRightV2(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        count, old_tail = 0, head  # count表示链表节点个数
        while old_tail.next:
            old_tail = old_tail.next
            count += 1
        old_tail.next = head  # 形成一个环
        new_tail = head
        # 本质还是求倒数第k各节点，如果k大于count，那就是k%count，如果小于count，那就是k，这种情况下k%count=k
        #
        for i in range(count - k % count):
           new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字
        :param head:
        :return:
        '''
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        while cur:
            if pre.val == cur.val:
                cur = cur.next
                pre.next = cur
            else:
                cur = cur.next
                pre = pre.next
        return head

    def hasCycle(self, head: ListNode) -> bool:
        '''判断链表是否有环'''
        if not head:
            return False
        fast = slow = head
        while fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        '''检测环的头结点'''
        if not head:
            return None
        fast = slow = head
        while fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

    def sortList(self, head: ListNode) -> ListNode:
        """
        https://leetcode-cn.com/problems/sort-list/
        在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序
        :param head:
        :return:
        """
        if head is None:
            return head
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        tmp = head
        res.sort()
        for i in res:
            tmp.val = i
            tmp = tmp.next
        return head
