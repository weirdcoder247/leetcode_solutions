class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        s = list(s)
        partition = [[s.pop(0)]]
        j = 0
        while(s != []):
            if partition[-1][j] in s:
                partition[-1].append(s.pop(0))
                print(j, partition)
            elif j < len(partition[-1]) - 1:
                j += 1
                print(j, len(partition[-1]), s)
            else:
                j = 0
                partition.append([s.pop(0)])
        return [len(x) for x in partition]


def main():
    s = input("Enter the string: ")
    obj = Solution()
    return obj.partitionLabels(s)

if __name__ == "__main__":
    print(main())
