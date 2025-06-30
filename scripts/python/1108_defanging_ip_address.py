class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")

if __name__ == '__main__':
    address = input("Enter the IP address: ")
    obj = Solution()
    print(obj.defangIPaddr(address))
