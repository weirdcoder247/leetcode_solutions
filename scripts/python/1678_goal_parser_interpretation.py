class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        target = ''
        command = list(command)
        curr_cmd = ''
        while(command != []):
            curr_cmd += command.pop(0)
            if curr_cmd == 'G':
                target += 'G'
                curr_cmd = ''
            elif curr_cmd == '()':
                target += 'o'
                curr_cmd = ''
            elif curr_cmd == '(al)':
                target +='al'
                curr_cmd = ''
        return target



def main():
    obj = Solution()
    command = input("Enter the command string: ")
    return obj.interpret(command)

if __name__ == "__main__":
    print(main())