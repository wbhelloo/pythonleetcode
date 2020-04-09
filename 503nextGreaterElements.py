from typing import List


class Solution:
    def nextGreaterElementsBL(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i + 1, n + i + 1):
                if j < n:
                    if nums[j] > nums[i]:
                        res.append(nums[j])
                        break
                else:
                    k = j - n
                    if nums[k] > nums[i]:
                        res.append(nums[k])
                        break
            else:
                res.append(-1)
        return res
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        stack = []
        res = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                small = stack.pop()
                res[small] = nums[i]
            stack.append(i)

        return res[:len(res)//2]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 1]
    print(sol.nextGreaterElements(nums))
