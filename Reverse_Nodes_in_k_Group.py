# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if k < 2:
            return head
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curr = head
        d = {}
        while curr:
            d['node0'] = curr
            for x in range(1, k):
                d['node{0}'.format(x)] = d['node{0}'.format(x-1)].next
                if not d['node{0}'.format(x)]:
                    return dummy.next
            d['node0'].next = d['node{0}'.format(k-1)].next
            prev.next = d['node{0}'.format(k-1)]
            for x in reversed(range(1, k)):
                d['node{0}'.format(x)].next = d['node{0}'.format(x-1)]
            curr = d['node0'].next
            prev = d['node0']
        return dummy.next
