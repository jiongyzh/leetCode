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

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    b = ListNode(7)
    b.next = ListNode(8)
    b.next.next = ListNode(9)
    r = Solution().addTwoNumbers(a, b)
    while r:
        print r.val
        r = r.next

