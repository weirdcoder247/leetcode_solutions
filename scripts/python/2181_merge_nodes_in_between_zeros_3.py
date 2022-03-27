# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head.next

        newhead = ListNode()
        newcur = newhead

        total = 0
        while cur is not None:
            while cur.val != 0:
                total += cur.val
                cur = cur.next

            newcur.next = ListNode(total)
            newcur = newcur.next
            cur = cur.next
            total = 0
        print(newcur.val, newhead.val)
        return newhead.next


