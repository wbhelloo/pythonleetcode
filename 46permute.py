from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        length = len(nums)

        res = [[nums[0]]]
        if length == 1:
            return res
        for i in range(1, length):
            prev = res.copy()
            res = []
            for tmp in prev:
                res.append(tmp + [nums[i]])
                for j in range(len(tmp)):
                    res.append(tmp[:j] + [nums[i]] + tmp[j:])
        return sorted(res)

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))
