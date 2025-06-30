from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        common_elem = [val for val in pairs[0] if val in pairs[1]]
        print(common_elem)
        s = list(s)
        s.append(s[pairs[0][0]])
        s[pairs[0][0]] = s[pairs[0][1]]
        s[pairs[0][1]] = s[-1]
        s = s[:-1]
        s.append(s[pairs[1][0]])
        s[pairs[1][0]] = s[pairs[1][1]]
        s[pairs[1][1]] = s[-1]
        s = s[:-1]
        return ''.join(s)


def main():
    s = input("Enter the string: ")
    import ast
    pairs = ast.literal_eval(input("Enter pairs as a list of lists: "))
    obj = Solution()
    return obj.smallestStringWithSwaps(s, pairs)


if __name__ == "__main__":
    print(main())

