class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        min_boat = 0
        people.sort(reverse=True)
        curr_boat = [0, 0]
        # itr = 0
        while(people != []):
            # itr += 1
            # print(min_boat, people, curr_boat)
            if people[0] >= limit:
                min_boat += 1
                people.pop(0)
            if curr_boat[0] != 2:
                if curr_boat[1] + people[0] <= limit:
                    curr_boat[0] += 1
                    curr_boat[1] += people.pop(0)
                elif curr_boat[1] + people[-1] <= limit:
                    curr_boat[0] += 1
                    curr_boat[1] += people.pop(-1)
                else:
                    min_boat += 1
                    curr_boat[0] = 1
                    curr_boat[1] = people.pop(0)
            elif curr_boat[0] == 2:
                min_boat += 1
                curr_boat = [0, 0]
        if curr_boat[0]:
            return min_boat + 1
        else:
            return min_boat


def main():
    people = [1,2]
    limit = 3
    people = [3,2,2,1]
    limit = 3
    people = [3,5,3,4]
    limit = 5
    people = [5,1,4,2]
    limit = 6
    obj = Solution()
    return obj.numRescueBoats(people, limit)

if __name__ == "__main__":
    print(main())
