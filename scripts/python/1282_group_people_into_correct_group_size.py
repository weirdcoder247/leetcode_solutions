class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        n = len(groupSizes)
        unique = set(groupSizes)
        target = []
        index = 0
        group_switch = {}
        for i in unique:
            group_switch[i] = []
        while(groupSizes != []):
            group_switch[groupSizes.pop(0)].append(index)
            index += 1
        for i in unique:
            if len(group_switch[i]) == i:
                target.append(group_switch[i])
                del group_switch[i]
            else:
                while(len(group_switch[i]) != 0):
                    target.append(group_switch[i][-i:])
                    del group_switch[i][-i:]

        return target


def main():
    obj = Solution()
    groupSizes = list(map(int, input("Enter group sizes separated by spaces: ").split()))
    return obj.groupThePeople(groupSizes)

if __name__ == "__main__":
    print(main())
