class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(set(sentence)) is 26:
            return True
        else:
            return False
