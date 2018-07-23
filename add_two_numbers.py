class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        lr = ListNode(0)
        lc = lr
        carry, sum_val = 0, 0
        while l1 or l2:
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            sum_val += carry
            carry = sum_val / 10
            sum_val = sum_val % 10
            lc.next = ListNode(sum_val)
            lc = lc.next
            sum_val = 0
        if carry > 0:
            lc.next = ListNode(1)
        return lr.next

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = l1
        p1 = l1
        while l1 and l2:
            carry1 = carry
            carry = (l1.val + l2.val + carry) / 10
            l1.val = (l1.val+l2.val+carry1) % 10
            p1 = l1
            l1 = l1.next
            l2 = l2.next
        if l2:
            p1.next = l2
            l1 = l2
        while l1:
            if l1.val + carry < 10:
                l1.val = l1.val + carry
                carry = 0
                break
            carry1 = carry
            carry = (l1.val+carry) / 10
            l1.val = (l1.val+carry1) % 10
            p1 = l1
            l1 = l1.next
        if carry > 0:
            p1.next = ListNode(carry)
        return l3

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    b = ListNode(7)
    b.next = ListNode(8)
    b.next.next = ListNode(9)
    b.next.next.next = ListNode(5)
    b.next.next.next.next = ListNode(4)
    r = Solution().addTwoNumbers2(a, b)
    while r:
        print r.val
        r = r.next
