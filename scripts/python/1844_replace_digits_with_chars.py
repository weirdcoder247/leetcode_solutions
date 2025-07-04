class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(len(s)):
            if ord(s[i]) < 97:
                s[i] = chr(ord(s[i-1]) + int(s[i]))
        return ''.join(s)

def main():
    s = input("Enter the string: ")
    obj = Solution()
    return obj.replaceDigits(s)

if __name__ == '__main__':
    print(main())
