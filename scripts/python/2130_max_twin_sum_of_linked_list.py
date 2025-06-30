from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def stringToListNode(self, input, pos=-1):
        # Generate list from the input
        import json
        numbers = json.loads(input)

        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        if 0 <= pos <= len(numbers) - 1:
            jugaadNode = ListNode(0)
            counter = -1
            for number in numbers:
                counter += 1
                ptr.next = ListNode(number)
                ptr = ptr.next
                if counter == pos:
                    jugaadNode = ptr
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

    def pairSum(self, head: Optional[ListNode]) -> int:
        reversed_head = self.reverseList(head)
        self.prettyPrintLinkedList(reversed_head)
        self.prettyPrintLinkedList(head) 


    def reverseList(self, head: ListNode) -> ListNode:
         if head == None or head.next == None:
            return head
         prev, curr = None, head
         while curr:
                self.prettyPrintLinkedList(curr)
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
         self.prettyPrintLinkedList(curr)
         return prev


def main():
    head = input("Enter the linked list as a JSON array (e.g., [5,4,2,1]): ")
    obj = Solution()
    head = obj.stringToListNode(head)
    obj.prettyPrintLinkedList(head)
    return obj.pairSum(head)
    
if __name__ == "__main__":
    print(main())

