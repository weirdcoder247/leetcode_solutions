class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        city_A = [0,0]
        city_B = [0,0]
        if sum([x[0] for x in costs]) >= sum([x[1] for x in costs]):
            costs.sort(reverse=True)
        else:
            costs.sort(key=lambda x: x[1], reverse=True)
        while(costs != []):
            if costs[0][0] >= costs[0][1]:
                if city_B[0] < n / 2:
                    city_B[0] += 1
                    city_B[1] += costs[0][1]
                    costs.pop(0)
                else:
                    city_A[0] += 1
                    city_A[1] += costs[0][0]
                    costs.pop(0)
            else:
                if city_A[0] < n / 2:
                    city_A[0] += 1
                    city_A[1] += costs[0][0]
                    costs.pop(0)
                else:
                    city_B[0] += 1
                    city_B[1] += costs[0][1]
                    costs.pop(0)
        return city_A[1] + city_B[1]

def main():
    costs = [[10,20],[30,200],[400,50],[30,20]] # 110
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]] # 1859
    costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]] # 3086
    # costs = [[100,10],[100,20],[90,10],[90,20],[110,10],[110,20]]
    obj = Solution()
    return obj.twoCitySchedCost(costs)

if __name__ == "__main__":
    print(main())
