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
    items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    return obj.countMatches(items, ruleKey, ruleValue)

if __name__ == '__main__':
    main()
