from typing import List


class Solution:
    def combinationSumGre(self, candidates, target, start, curr, res):
        if start >= len(candidates):
            return
        if sum(curr) > target:
            return
        if sum(curr) == target:
            res.append(curr.copy())
            return
        tmp = candidates[start] + sum(curr)
        if tmp <= target:
            curr.append(candidates[start])
            self.combinationSumGre(candidates, target, start, curr, res)
            curr.pop(-1)
        self.combinationSumGre(candidates, target, start + 1, curr, res)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        self.combinationSumGre(candidates, target, 0, [], res)
        return res


if __name__ == '__main__':
    sol = Solution()
    candidates = [8, 7, 4, 3]
    target = 11
    print(sol.combinationSum(candidates, target))
