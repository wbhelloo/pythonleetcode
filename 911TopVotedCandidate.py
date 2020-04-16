from typing import List
from collections import OrderedDict


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        def helper(persons, times):

            res = []
            personsCount = dict()
            max = persons[0]
            for person in persons:
                personsCount[person] = personsCount.get(person, 0) + 1
                if personsCount[person] >= personsCount[max]:
                    max = person
                res.append(max)
            top = [0 for _ in range(times[-1] + 1)]
            i, j = 0, times[0]
            while i < len(times) - 1 and j < len(top):
                if times[i] <= j < times[i + 1]:
                    top[j] = res[i]
                    j += 1
                else:
                    i += 1
            while j < len(top):
                top[j] = res[i]
                j += 1

            return top

        self.dp = helper(persons, times)

    def q(self, t: int) -> int:
        if t < len(self.dp):
            return self.dp[t]
        else:
            return self.dp[-1]


# Your TopVotedCandidate object will be instantiated and called as such:
if __name__ == '__main__':
    persons = [0, 0, 1, 1, 2]
    times = [0, 67, 69, 74, 87]
    obj = TopVotedCandidate(persons, times)
    ts = [[4], [62], [100], [88], [70], [73], [22], [75], [29], [10]]
    res = []
    for t in ts:
        res.append(obj.q(*t))
    print(res)
