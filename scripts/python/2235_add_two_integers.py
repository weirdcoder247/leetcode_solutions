class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

def main():
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    obj = Solution()
    return obj.sum(num1, num2)

if __name__ == "__main__":
    print(main())

