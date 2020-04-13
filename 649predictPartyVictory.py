from collections import Counter
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senates = list(senate)
        dcount = 0
        while 'D' in senates and "R" in senates:
            tmp = []
            for s in senates:
                if s == 'D':
                    if dcount >= 0:
                        tmp.append(s)
                    dcount+=1
                else:
                    if dcount <= 0:
                        tmp.append(s)
                    dcount-=1
            senates = tmp

        if 'D' in senates:
            return "Dire"
        if "R" in senates:
            return "Radiant"



if __name__ == '__main__':
    sol = Solution()
    sen = "RD"
    print(sol.predictPartyVictory(sen))
