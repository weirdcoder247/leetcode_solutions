# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def append(res_t=ListNode(), append=0):
    # print("Append Called")
    # print(res_t.val, res_t.next)
    if ln_len(res_t) > 1:
        exec("res_t" + ".next" * (ln_len(res_t)) + " = ListNode(append)")
    elif ln_len(res_t) == 1 and res_t.val == 0:
        res_t.val = append
        res_t.next = None
    elif ln_len(res_t) == 1 and res_t.val != 0:
        res_t.next = ListNode(append)
    # print(res_t.val, res_t.next)
    return res_t

def ln_len(obj=ListNode()):
    """
    :rtype: int()
    """
    if obj is not None:
        if type(obj.next) == None:
            return 1
        else:
            return 1 + ln_len(obj.next)
    else:
        return 0


class Solution(object):
    def __init__(self, cum_sum_g=0, ln=ListNode(0, None)):
        self.cum_sum_g = cum_sum_g
        self.ln = ln

    def mergeNodes(self, obj_l=ListNode()):
        # self.counter = self.counter + 1
        # print("func call", self.counter)
        if obj_l.val == 0 and obj_l.next is not None:
            # print("1", ln_len(self.ln), self.ln.val, self.ln.next)
            # self.ln = obj_l
            if self.cum_sum_g > 0:
                # print("before append")
                # print(self.ln.val, self.ln.next)
                self.ln = append(self.ln, self.cum_sum_g)
                # print("after append")
                # print(self.ln.val, self.ln.next)
                self.cum_sum_g = 0
            self.mergeNodes(obj_l.next)
            return self.ln
        elif obj_l.val == 0 and obj_l.next is None:
            # print("2", ln_len(self.ln), self.ln.val, self.ln.next)
            # self.ln = obj_l
            if self.cum_sum_g > 0:
                # print("before append")
                # print(self.ln.val, self.ln.next)
                self.ln = append(self.ln, self.cum_sum_g)
                # print("after append")
                # print(self.ln.val, self.ln.next)
                self.cum_sum_g = 0
            return
        elif obj_l.val != 0:
            # print("3", ln_len(self.ln), self.ln.val, self.ln.next)
            self.cum_sum_g = self.cum_sum_g + obj_l.val
            self.mergeNodes(obj_l.next)
        return



if __name__ == '__main__':
    obj = Solution(0, ListNode(0, None))
    # head = ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(0, ListNode(5, ListNode(0, None)))))))
    # head = ListNode(0, ListNode(1, ListNode(0, None)))
    # head = ListNode(0, ListNode(1, ListNode(1, ListNode(0, None))))
    head = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0, None))))))))
    obj.mergeNodes(head)
    print(ln_len(obj.ln))
