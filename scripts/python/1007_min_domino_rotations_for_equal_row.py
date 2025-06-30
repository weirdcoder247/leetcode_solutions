class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        l_top = len(set(tops))
        l_bottom = len(set(bottoms))
        if l_top == 1 or l_bottom == 1:
            return 0
        else:
            if l_top <= l_bottom:
                first = tops
                second = bottoms
            else:
                first = bottoms
                second = bottoms
            first_rotations = 0
            second_rotations = 0
            flag = True
            i = 0
            while(flag and i < l_top):
                print(first, second)
                if first[i] != first[i + 1] and first[i] == second[i + 1]:
                    first[i + 1] = second[i + 1]
                    first_rotations += 1
                    i += 1
                    if len(set(first)) == 1:
                        return first_rotations
                elif second[i] != second[i + 1] and second[i] == first[i + 1]:
                    second[i + 1] = first[i + 1]
                    second_rotations += 1
                    i += 1
                    if len(set(second)) == 1:
                        return second_rotations
                else:
                    return -1
                print(first, second)

def main():
    tops = list(map(int, input("Enter tops separated by spaces: ").split()))
    bottoms = list(map(int, input("Enter bottoms separated by spaces: ").split()))
    obj = Solution()
    return obj.minDominoRotations(tops, bottoms)

if __name__ == "__main__":
    print(main())
