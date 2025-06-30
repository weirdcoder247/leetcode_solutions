class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        ans = 0
        dict_LR = {
            'L': 0,
            'R': 0
        }
        l_c = 0
        r_c = 0
        while s != []:
            if s[0] == 'L':
                l_c += 1
            elif s[0] == 'R':
                r_c += 1
            s.pop(0)
            if 0 < l_c == r_c > 0:
                ans += 1
                l_c = 0
                r_c = 0
            # dict_LR[s.pop(0)] += 1
            # if dict_LR['L'] == dict_LR['R'] > 0:
            #     ans += 1
            #     dict_LR = {
            #         'L': 0,
            #         'R': 0
            #     }
        return ans


def main():
    obj = Solution()
    s = input("Enter the string: ")
    return obj.balancedStringSplit(s)

if __name__ == "__main__":
    print(main())
