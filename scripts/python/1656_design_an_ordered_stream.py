class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.stream = [None for i in range(n)]
        self.ptr = 0


    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey - 1] = value
        ans = []
        while(self.ptr < self.n and self.stream[self.ptr] is not None):
            ans.append(self.stream[self.ptr])
            self.ptr += 1
        return ans

