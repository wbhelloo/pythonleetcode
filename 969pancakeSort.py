from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []

        def helper(nums, end):
            if end < 0:
                return
            nonlocal res

            max = end - 1
            for i in range(end - 1):
                if nums[i] > nums[max]:
                    max = i
            if max == end - 1:
                helper(nums, end - 1)
            else:
                res.append(max + 1)
                nums = nums[:max + 1][::-1] + nums[max + 1:end]
                res.append(end)
                nums = nums[::-1]
                helper(nums, end - 1)

        helper(A, len(A))
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 4, 2, 3]
    print(sol.pancakeSort(nums))
