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
    candies = [2,3,5,1,3]
    extraCandies = 3
    obj = Solution()
    obj.kidsWithCandies(candies, extraCandies)
