class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        [pref is w[:len(pref)] for w in words]
        return sum([pref == w[:len(pref)] for w in words])

def main():
    words = input("Enter words separated by spaces: ").split()
    pref = input("Enter prefix: ")
    obj = Solution()
    return obj.prefixCount(words, pref)

if __name__ == '__main__':
    print(main())
