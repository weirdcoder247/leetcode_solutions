class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        beams = 0
        bank_len = len(bank)
        if bank_len == 1:
            return 0
        else:
            i = 0
            j = 1
            while(j < bank_len):
                # does row i have any lasers?
                sum_lasers_i = sum([int(x) for x in bank[i]])
                if sum_lasers_i == 0:
                    i += 1
                    j = i + 1
                else:
                    # does row j have any lasers?
                    sum_lasers_j = sum([int(x) for x in bank[j]])
                    if sum_lasers_j == 0:
                        j += 1
                    else:
                        beams += sum_lasers_i * sum_lasers_j
                        i = j
                        j += 1
            return beams


def main():
    bank = input("Enter bank rows separated by spaces (e.g., 011001 000000 010100 001000): ").split()
    obj = Solution()
    return obj.numberOfBeams(bank)

if __name__ == "__main__":
    print(main())
