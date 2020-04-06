from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        dp = [0 for _ in range(length)]
        dp[0] = nums[0]
        for i in range(1, length):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, -1]
    print(sol.maxSubArray(nums))
