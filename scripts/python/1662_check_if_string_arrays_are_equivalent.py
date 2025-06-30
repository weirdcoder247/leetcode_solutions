class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1 = ""
        for i in word1:
            w1 += i
        w2 = ""
        for i in word2:
            w2 += i
        return w1 == w2

    def arrayStringsAreEqual2(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return "".join(word1) == "".join(word2)

def main():
    word1 = input("Enter word1 as space-separated strings: ").split()
    word2 = input("Enter word2 as space-separated strings: ").split()
    obj = Solution()
    return obj.arrayStringsAreEqual2(word1, word2)

if __name__ == "__main__":
    print(main())
