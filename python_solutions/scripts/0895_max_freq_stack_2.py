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
    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())


if __name__ == '__main__':
    print(main())
