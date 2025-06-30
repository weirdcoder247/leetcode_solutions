class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        return [(candies[x] + extraCandies) >= max(candies) \
            for x in range(len(candies))]



if __name__ == '__main__':
    candies = list(map(int, input("Enter candies separated by spaces: ").split()))
    extraCandies = int(input("Enter extraCandies: "))
    obj = Solution()
    obj.kidsWithCandies(candies, extraCandies)
