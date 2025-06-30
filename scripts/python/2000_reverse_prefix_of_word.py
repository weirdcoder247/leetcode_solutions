class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ch_index = word.find(ch)
        if ch_index is not -1:
            return word[ch_index::-1] + word[ch_index + 1::]
        return word

def main():
    word = input("Enter the word: ")
    ch = input("Enter the character: ")
    obj = Solution()
    return obj.reversePrefix(word, ch)

if __name__ == "__main__":
    print(main())
