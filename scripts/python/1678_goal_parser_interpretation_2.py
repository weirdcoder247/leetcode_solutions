class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        switcher = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al'
        }
        target = ''
        command = list(command)
        curr_cmd = ''
        while(command != []):
            curr_cmd += command.pop(0)
            case = switcher.get(curr_cmd)
            if case is not None:
                target += case
                curr_cmd = ''
        return target



def main():
    obj = Solution()
    command = input("Enter the command string: ")
    return obj.interpret(command)

if __name__ == "__main__":
    print(main())