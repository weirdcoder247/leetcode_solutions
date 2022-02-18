class Solution(object):

    # def __init__(self):
    #     partition_counter = 0

    partition_counter = 0
    rec_call_counter = 0
    mod = -1

    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        l = len(str(n))
        # global partition_counter
        # for i in range(int(bin(pow(2, l - 1))[2:]), int(bin(pow(2, l) - 1)[2:])):
        #     print(i)
        for i in range(pow(2, l) - 1, pow(2, l - 1) - 1, -1):
            print("iteration i =", i, "n =", n)
            bin_num = int(bin(i)[2:])
            print(bin_num)
            div_float = n / bin_num
            print(div_float)
            self.mod = n % bin_num
            if (div_float >= 1.0):
                print("div_float =", div_float)
                print("mod =", self.mod)
                # self.mod = n % bin_num
                self.partition_counter = self.partition_counter + int(div_float)
                print("partition_counter =", self.partition_counter)
                check = False
                while(self.mod != 0):
                    check = True
                    print("inside while loop")
                    self.rec_call_counter = self.rec_call_counter + 1
                    recall_iteration = self.rec_call_counter
                    print("Recursive Call: ", recall_iteration, " Start; n =", n, "mod =", self.mod)
                    self.minPartitions(n = self.mod)
                    print("Recursive Call: ", recall_iteration, " End; n =", n, "mod =", self.mod)
                # return self.partition_counter
                if check is True:
                    print("while loop exit")
                elif check is False:
                    print("while loop skip")
                if self.mod == 0:
                    print("break 1 triggered")
                    break
                print("break 2 triggered")
                break
            else:
                print("continue triggered")
                continue
            if self.mod == 0:
                print("break 3 triggered")
                break
        print("main return statement")
        return self.partition_counter



if __name__ == '__main__':
    # n = 82734
    n = 27346209830709182346
    obj = Solution()
    obj.minPartitions(n)



# for i in range(10):
#     # print(i, bin(i)[2:], len(bin(i)[2:]))
#     bin(pow(2, i)-1)[2:]
#     # print(bin(pow(2,i)-1[2:]), len(bin(pow(2,i)-1)[2:]))

# n = 1001
# l = len(str(n))
# int(bin(pow(2, l)-1)[2:])
# n/int(bin(pow(2, l)-1)[2:]) >= 1
# n/int(bin(pow(2, l)-7)[2:]) >= 1

# n % int(bin(pow(2, l)-1)[2:])
# n % int(bin(pow(2, l-1))[2:])
# n / int(bin(pow(2, l)-1)[2:])
# n / int(bin(pow(2, l-1))[2:])

# int(bin(pow(2, l)-1)[2:])
# int(bin(pow(2, l-1))[2:])
