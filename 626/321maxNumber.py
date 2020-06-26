from typing import List
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def MaxNumberK(nums, K):
            drop = len(nums) - K
            stack = []
            for num in nums:
                while stack and stack[-1] < num and drop > 0:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:K]

        def merge(s1, s2):
            if not s1 or not s2:
                return s1 + s2
            if s1 < s2:
                s1, s2 = s2, s1
            if s1[0] >= s2[0]:
                return [s1[0]] + merge(s1[1:], s2)
            else:
                return [s2[0]] + merge(s1, s2[1:])

        res = [merge(MaxNumberK(nums1, i), MaxNumberK(nums2, k - i)) for i in range(k + 1)]
        return max(r for r in res if len(r) == k)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxNumber(nums1=[2, 5, 6, 4, 4, 0], nums2=[7, 3, 8, 0, 6, 5, 7, 6, 2], k=15))
