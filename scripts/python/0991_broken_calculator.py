class Solution(object):
   def brokenCalc(self, X, Y):
      res = 0
      while Y > X:
         res += Y % 2 + 1
         Y = Y // 2 if Y % 2 == 0 else (Y + 1)//2
      return res + X - Y

def main():
    startValue = int(input("Enter startValue: "))
    target = int(input("Enter target: "))
    obj = Solution()
    return obj.brokenCalc(startValue, target)

if __name__ == "__main__":
    print(main())
