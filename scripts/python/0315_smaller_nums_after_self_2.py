class Solution(object):
    def countSmaller(self, nums):
        nums = nums[::-1]
        nums = [(n,i) for i,n in enumerate(nums)]
        res = [0]*len(nums)

        def mergesort(l,r):
            if l == r:
                return
            mid = (l+r)//2
            mergesort(l,mid)
            mergesort(mid+1,r)

            i = l
            # O(n)
            for j in range(mid+1,r+1):
                while i < mid+1 and nums[i][0] < nums[j][0]:
                    i += 1
                res[nums[j][1]] += i-l

            nums[l:r+1] = sorted(nums[l:r+1])

        mergesort(0,len(nums)-1) if nums else None
        return res[::-1]

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj = Solution()
    print(obj.countSmaller(nums))

if __name__ == "__main__":
    main()
