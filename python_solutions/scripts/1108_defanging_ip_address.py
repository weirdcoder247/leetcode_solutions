class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")

if __name__ == '__main__':
    address = "0.0.0.0"
    obj = Solution()
    obj.defangIPaddr(address)
