class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(set(s))
        s.sort()
        ans = ''
        for i in s:
            ans += i
        return ans

def main():
    s = "bcabc"
    obj = Solution()
    return obj.removeDuplicateLetters(s)

if __name__ == '__main__':
    print(main())
