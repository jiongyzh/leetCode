# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        res = ListNode(None)
        res.next = head
        cur = prob = res

        for _ in range(n):
            prob = prob.next

        while prob.next:
            cur = cur.next
            prob = prob.next

        cur.next = cur.next.next

        return res.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    r = Solution().removeNthFromEnd(a, 2)
    while r:
        print r.val
        r = r.next