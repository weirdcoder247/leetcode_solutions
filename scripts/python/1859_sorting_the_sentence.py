class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        lookUp = {}
        for i in s:
            lookUp[int(i[-1:])] = i[:-1]
        ans = ''
        for i in range(1, len(lookUp) + 1):
            ans += lookUp[i] + ' '
        return ans.strip()


def main():
    obj = Solution()
    s = input("Enter the sentence to sort: ")
    return obj.sortSentence(s)


if __name__ == "__main__":
    main()
