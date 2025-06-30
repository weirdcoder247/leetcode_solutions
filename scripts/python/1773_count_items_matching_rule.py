class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        rule_dict = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        return (sum([x[rule_dict[ruleKey]] == ruleValue for x in items]))


def main():
    obj = Solution()
    import ast
    items = ast.literal_eval(input("Enter items as a list of lists: "))
    ruleKey = input("Enter ruleKey (type/color/name): ")
    ruleValue = input("Enter ruleValue: ")
    return obj.countMatches(items, ruleKey, ruleValue)

if __name__ == '__main__':
    main()
