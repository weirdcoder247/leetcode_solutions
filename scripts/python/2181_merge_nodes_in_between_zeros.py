# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        if type(self.next) == type(int()):
            self.length = 1
        else:
            self.length = -1

    def append(self, append):
        if ln_len(self) > 1:
            exec("self" + ".next" * (ln_len(self) - 1) + " = ListNode(self" + ".next" * (ln_len(self) - 1) + ", append)")
        elif ln_len(self) == 1 and self.val == 0:
            self.val = append
            self.next = None
        elif ln_len(self) == 1 and self.val != 0:
            self.next = append



def ln_len(obj=ListNode()):
    """
    :rtype: int()
    """
    if obj is not None:
        if type(obj.next) == type(int()):
            return 2
        elif type(obj.next) == None:
            return 1
        else:
            return 1 + ln_len(obj.next)
    else:
        return 0


class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = ln_len(head)
        if l == 3:
            print("l =", l)
            return ListNode(head.next.val, None)
        elif l == 4:
            print("l =", l)
            return ListNode(head.next.val + head.next.next.val, None)
        elif l >= 5:
            print("l =", l)
            counter = 0
            res = ListNode()
            head_temp = head
            cum_sum = 0
            while counter < (l - 1):
                # print(counter, head_temp.val, head_temp.next.val)
                print(counter, "res:", res.val, res.next, cum_sum)
                # res = res.append(head.next)
                if type(head_temp.next) == type(ListNode()):
                    if head_temp.val == 0:
                        if counter != 0:
                            # res.append(cum_sum)
                            print("NOT appended res2:", ln_len(res), res.val)
                            head_temp = head_temp.next
                            cum_sum = 0
                            counter = counter + 1
                        else:
                            counter = counter + 1
                            head_temp = head_temp.next
                    elif head_temp.val != 0 and head_temp.next.val != 0:
                        cum_sum = cum_sum + head_temp.val
                        head_temp = head_temp.next
                        counter = counter + 1
                        print("cum_sum incremented!", cum_sum, ln_len(head_temp), counter)
                    elif head_temp.val != 0 and head_temp.next.val == 0:
                        cum_sum = cum_sum + head_temp.val
                        res.append(cum_sum)
                        cum_sum = 0
                        print("appended res1:", ln_len(res), res.val)
                        head_temp = head_temp.next
                        counter = counter + 1
                elif type(head_temp.next) == type(int()):
                    if head_temp.val != 0 and head_temp.next == 0:
                        cum_sum = cum_sum + head_temp.val
                        res.append(cum_sum)
                        cum_sum = 0
                        print("appended res3:", ln_len(res), res.val)
                        # print("appended res3:", ln_len(res), res.val, res.next.val)
                        counter = counter + 1
                        break
            return res



if __name__ == '__main__':
    obj = Solution()
    # head = ListNode(0, ListNode(1, ListNode(0, ListNode(1, ListNode(1, ListNode(0, ListNode(2, 0)))))))
    # head = ListNode(0, ListNode(1, ListNode(2, 0)))
    # head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, 0))))
    # [0,3,1,0,4,5,2,0]
    head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, 0)))))))
    obj.mergeNodes(head)
