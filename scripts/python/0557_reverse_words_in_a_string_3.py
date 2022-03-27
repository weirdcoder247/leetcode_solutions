class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        ans = ""
        for w in s:
            ans += w[::-1] + " "
        return ans[:-1]

def main():
    s = "Let's take LeetCode contest"
    obj = Solution()
    return obj.reverseWords(s)

if __name__ == '__main__':
    print(main())
