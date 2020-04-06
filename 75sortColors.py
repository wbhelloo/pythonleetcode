from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        high = len(nums) - 1
        low = 0
        i = 0
        while i <= high:
            if nums[i] == 0:
                if i != low:
                    nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    print(nums)
