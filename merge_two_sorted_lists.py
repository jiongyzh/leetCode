# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = cur = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return res.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    b.next.next.next = ListNode(5)
    b.next.next.next.next = ListNode(6)
    r = Solution().mergeTwoLists(a, b)
    while r:
        print r.val
        r = r.next