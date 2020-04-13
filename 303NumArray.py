from typing import List


class NumArray:

    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    #
    # def sumRange(self, i: int, j: int) -> int:
    #     return sum(self.nums[i:j+1])

    def __init__(self, nums: List[int]):
        self.res = [0]
        for i in range(len(nums)):
            self.res.append(nums[i] + self.res[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.res[j + 1] - self.res[i]


# Your NumArray object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))
