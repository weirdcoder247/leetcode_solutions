class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        s = list(s)
        st = ''
        str_len = len(indices)
        tup_list = [(s[i], indices[i]) for i in range(str_len)]
        tup_list.sort(key = lambda x: x[1])
        for i in range(str_len):
            st += tup_list[i][0]
        return st

if __name__ == '__main__':
    obj = Solution()
    s = input("Enter the string: ")
    indices = list(map(int, input("Enter indices separated by spaces: ").split()))
    obj.restoreString(s, indices)
