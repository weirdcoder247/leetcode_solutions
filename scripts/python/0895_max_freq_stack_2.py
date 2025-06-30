class FreqStack:
    def __init__(self):
        from collections import Counter, defaultdict
        self.maxFreq = 0
        self.count = Counter()
        self.countToStack = defaultdict(list)

    def push(self, val):
        self.count[val] += 1
        self.countToStack[self.count[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.count[val])

    def pop(self):
        val = self.countToStack[self.maxFreq].pop()
        self.count[val] -= 1
        if not self.countToStack[self.maxFreq]:
            self.maxFreq -= 1
        return val


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
