class Solution(object):
   def brokenCalc(self, X, Y):
      res = 0
      while Y > X:
         res += Y % 2 + 1
         Y = Y // 2 if Y % 2 == 0 else (Y + 1)//2
      return res + X - Y

def main():
    startValue = 2
    target = 3
    startValue = 5
    target = 8
    startValue = 3
    target = 10
    startValue = 1
    target = 1000000000
    startValue = 1000000000
    target = 1
    obj = Solution()
    return obj.brokenCalc(startValue, target)

if __name__ == "__main__":
    print(main())
