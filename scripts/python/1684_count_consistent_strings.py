class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        str_count = 0
        for i in words:
            flag = True
            str_count += 1
            for j in i:
                if j not in allowed:
                    flag = False
                    str_count -= 1
                    break
        return str_count

def main():
    allowed = input("Enter allowed characters: ")
    words = input("Enter words separated by spaces: ").split()
    obj = Solution()
    return obj.countConsistentStrings(allowed, words)

if __name__ == '__main__':
    print(main())
