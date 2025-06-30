class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        [arr.append(encoded[i]^arr[i]) for i in range(len(encoded))]
        return arr

if __name__ == '__main__':
    obj = Solution()
    encoded = list(map(int, input("Enter encoded array separated by spaces: ").split()))
    first = int(input("Enter first: "))
    obj.decode(encoded, first)