# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        all_node_vals = []
        head = current = ListNode(0)
        for l in lists:
            while l:
                all_node_vals.append(l.val)
                l = l.next
        all_node_vals.sort()
        for node_val in all_node_vals:
            current.next = ListNode(node_val)
            current = current.next
        return head.next
