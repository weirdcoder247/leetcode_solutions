class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.split(" ")
        ans = ""
        for i in range(k):
            ans += s[i] + " "
        return ans[:-1]


def main():
    s = "Hello how are you Contestant"
    k = 4
    obj = Solution()
    return obj.truncateSentence(s, k)

if __name__ == '__main__':
    print(main())
