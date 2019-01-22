# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            first = curr.next
            if not first:
                return dummy.next
            second = curr
            third = first.next
            first.next = second
            second.next = third
            prev.next = first
            curr = third
            prev = second
        return dummy.next
