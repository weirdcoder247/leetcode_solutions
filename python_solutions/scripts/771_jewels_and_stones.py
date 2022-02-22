class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = list(jewels)
        stones = list(stones)
        res = 0
        # # Approach 1
        # for i in range(len(jewels)):
        #     res = res + sum([stones[x] == jewels[i] for x in range(len(stones))])
        # return res

        # Approach 2
        return sum([stones[x] == jewels[i] for x in range(len(stones)) for i in range(len(jewels))])



if __name__ == '__main__':
    obj = Solution()
    jewels = "aA"
    stones = "aaaaAAAddsdsds"
    obj.numJewelsInStones(jewels, stones)
