class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max([len(x) for x in [x.split() for x in sentences]])

if __name__ == '__main__':
    sentences = input("Enter sentences separated by ';': ").split(';')
    obj = Solution()
    obj.mostWordsFound(sentences)
