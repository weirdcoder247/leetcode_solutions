class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_dict = dict.fromkeys(set(s), 0)
        for i in s:
            char_dict[i] += 1

        return len(set(char_dict.values())) is 1

def main():
    s = input("Enter the string: ")
    obj = Solution()
    return obj.areOccurrencesEqual(s)

if __name__ == '__main__':
    print(main())
