# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        n = len(groupSizes)
        unique = set(groupSizes)
        target = []
        index = 0
        group_switch = {}
        for i in unique:
            group_switch[i] = []
        while(groupSizes != []):
            group_switch[groupSizes.pop(0)].append(index)
            index += 1
        for i in unique:
            if len(group_switch[i]) == i:
                target.append(group_switch[i])
                del group_switch[i]
            else:
                while(len(group_switch[i]) != 0):
                    target.append(group_switch[i][-i:])
                    del group_switch[i][-i:]

        return target

    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        arr = np.array(grid)
        row_max = arr.max(axis=1)
        col_max = arr.max(axis=0)
        n = len(grid)
        m = max([len(x) for x in grid])
        res = 0
        for i in range(n):
            for j in range(m):
                res += (min(row_max[i], col_max[j]) - grid[i][j])
        return res

    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        ans = 0
        dict_LR = {
            'L': 0,
            'R': 0
        }
        l_c = 0
        r_c = 0
        while s != []:
            if s[0] == 'L':
                l_c += 1
            elif s[0] == 'R':
                r_c += 1
            s.pop(0)
            if 0 < l_c == r_c > 0:
                ans += 1
                l_c = 0
                r_c = 0
            # dict_LR[s.pop(0)] += 1
            # if dict_LR['L'] == dict_LR['R'] > 0:
            #     ans += 1
            #     dict_LR = {
            #         'L': 0,
            #         'R': 0
            #     }
        return ans

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

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        slow = head
        fast = head.next
        while(slow != fast):
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True



def main():
    # obj = Solution()
    # groupSizes = [3,3,3,3,3,1,3]
    # return obj.groupThePeople(groupSizes)
    # obj = Solution()
    # grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    # return obj.maxIncreaseKeepingSkyline(grid)
    # obj = Solution()
    # s = 'LLLRRRLRLLRR'
    # return obj.balancedStringSplit(s)
    obj = Solution()
    s = "[3,2,0,-4]"
    pos = 22
    head = obj.stringToListNode(s, pos)
    return obj.hasCycle(head)

if __name__ == "__main__":
    print(main())
