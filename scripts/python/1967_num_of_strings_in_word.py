class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        return sum([x in word for x in patterns])

def main():
    patterns = input("Enter patterns separated by spaces: ").split()
    word = input("Enter the word: ")
    obj = Solution()
    return obj.numOfStrings(patterns, word)

if __name__ == '__main__':
    print(main())
