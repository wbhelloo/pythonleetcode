from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # dp[j][0]代表以j结尾的最后一个为下降的最长序列
        # dp[j][1]代表以j结尾的最后一个为上升的最长序列
        dp = [[1 for _ in range(2)] for _ in range(len(nums))]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                while j >= 0 and nums[j] <= nums[i]:
                    j -= 1
                if j >= 0:
                    dp[i][0] = max(dp[j][1] + 1, dp[i][0])
                j -= 1

            k = i - 1
            while k >= 0:
                while k >= 0 and nums[k] >= nums[i]:
                    k -= 1
                if k >= 0:
                    dp[i][1] = max(dp[k][0] + 1, dp[i][1])
                k -= 1
        return max(dp[i][j] for i in range(len(nums)) for j in range(2))


if __name__ == '__main__':
    sol = Solution()
    num = [33, 53, 12, 64, 50, 41, 45, 21, 97, 35, 47, 92, 39, 0, 93, 55, 40, 46, 69, 42, 6, 95, 51, 68, 72, 9, 32, 84,
           34, 64, 6, 2, 26, 98, 3, 43, 30, 60, 3, 68, 82, 9, 97, 19, 27, 98, 99, 4, 30, 96, 37, 9, 78, 43, 64, 4, 65,
           30, 84, 90, 87, 64, 18, 50, 60, 1, 40, 32, 48, 50, 76, 100, 57, 29, 63, 53, 46, 57, 93, 98, 42, 80, 82, 9,
           41, 55, 69, 84, 82, 79, 30, 79, 18, 97, 67, 23, 52, 38, 74, 15]
    num2 = [0, 0]
    print(sol.wiggleMaxLength(num))
