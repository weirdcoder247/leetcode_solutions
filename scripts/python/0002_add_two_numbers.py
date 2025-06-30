import json

from typing import Optional

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next: Optional['ListNode'] = None

class Solution(object):
    def stringToListNode(self, input, pos=-1):
        # Generate list from the input
        numbers = json.loads(input)

        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        if 0 <= pos <= len(numbers) - 1:
            jugaadNode = ListNode(0)
            counter = -1
            for number in numbers:
                counter += 1
                if ptr is not None:
                    ptr.next = ListNode(number)
                    ptr = ptr.next
                if counter == pos:
                    jugaadNode = ptr
            if ptr is not None:
                ptr.next = jugaadNode
            ptr = dummyRoot.next
            return ptr
        else:
            for number in numbers:
                ptr.next = ListNode(number)
                ptr = ptr.next
            ptr = dummyRoot.next
            return ptr

    def prettyPrintLinkedList(self, node):
        import sys
        while node and node.next:
            sys.stdout.write(str(node.val) + "->")
            node = node.next

        if node:
            print(node.val)
        else:
            print("Empty LinkedList")

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carryOver = 0
        while (l1 or l2 or carryOver > 0):
            if l1 is None:
                a = None
            else:
                a = l1.val
            if l2 is None:
                b = None
            else:
                b = l2.val
            x = [a, b, carryOver]
            curr.next = ListNode(sum([i for i in x if i is not None]) % 10)
            carryOver = int((sum([i for i in x if i is not None])) / 10)
            curr = curr.next
            if l1 and l1.next is not None:
                l1 = l1.next
            else:
                l1 = None
            if l2 and l2.next is not None:
                l2 = l2.next
            else:
                l2 = None
        return dummy.next

def main():
    obj = Solution()
    l1_str = input("Enter the first linked list as a JSON array (e.g., [2,4,3]): ")
    l2_str = input("Enter the second linked list as a JSON array (e.g., [5,6,4]): ")
    l1 = obj.stringToListNode(l1_str)
    l2 = obj.stringToListNode(l2_str)
    result = obj.addTwoNumbers(l1, l2)
    obj.prettyPrintLinkedList(result)

if __name__ == "__main__":
    main()
