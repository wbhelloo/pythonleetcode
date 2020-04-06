from typing import List


# 找到第一个插入target的位置，和最后一个插入target的位置
class Solution:
    def searchRangeK(self, nums, start, end, target):
        if start >= end:
            return end

        mid = (start + end) // 2
        if nums[mid] == target:
            if mid - 1 >= 0 and nums[mid - 1] == target:
                return self.searchRangeK(nums, start, end - 1, target)
            else:
                return mid
        elif nums[mid] > target:
            return self.searchRangeK(nums, start, end - 1, target)
        else:
            return self.searchRangeK(nums, mid + 1, end, target)

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        start = self.searchRangeK(nums, 0, len(nums), target)
        end = self.searchRangeK(nums, 0, len(nums), target + 1) - 1

        if start <len(nums) and nums[start] == target and end < len(nums) and nums[end] == target:
            return [start, end]
        elif start <len(nums) and nums[start] == target:
            return [start, start]
        else:
            return [-1, -1]


if __name__ == '__main__':
    sol = Solution()
    sol.nums = [5, 7, 7, 8, 8, 10]
    sol.target = 11
    print(sol.searchRange(sol.nums, sol.target))
