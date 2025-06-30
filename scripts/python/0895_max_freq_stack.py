class FreqStack(object):

    def __init__(self):
        self.stack = []
        self.stack_set = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val in self.stack_set:
            self.stack_set[val] += 1
        else:
            self.stack_set[val] = 1

    def pop(self):
        """
        :rtype: int
        """
        max_value = max(self.stack_set.values())
        max_key = [[i, self.stack_set[i] == max_value] for i in self.stack_set]
        max_key = [x[0] for x in max_key if x[1]]
        if len(max_key) == 1:
            self.stack.reverse()
            self.stack.remove(max_key[0])
            self.stack.reverse()
            self.stack_set[max_key[0]] -= 1
            return max_key[0]
        else:
            for i in reversed(self.stack):
                if i in max_key:
                    self.stack.reverse()
                    self.stack.remove(i)
                    self.stack.reverse()
                    self.stack_set[i] -= 1
                    return i
        return max_key


def main():
    obj = FreqStack()
    n = int(input("Enter number of operations: "))
    for _ in range(n):
        op = input("Enter operation (push <val>/pop): ").strip().split()
        if op[0] == "push":
            obj.push(int(op[1]))
        elif op[0] == "pop":
            print(obj.pop())


if __name__ == '__main__':
    print(main())
