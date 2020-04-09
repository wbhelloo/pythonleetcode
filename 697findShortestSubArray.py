from typing import List
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = max(count.values())
        keys = []
        for key, num in count.items():
            if num == n:
                keys.append(key)
        res = float('inf')
        for k in keys:
            begin = 0
            end = len(nums) - 1
            while begin <= end:
                if nums[begin] != k:
                    begin += 1
                    continue
                if nums[end] != k:
                    end -= 1
                    continue
                if res > end - begin:
                    res = end - begin + 1
                break
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2, 3, 1]
    print(sol.findShortestSubArray(nums))
