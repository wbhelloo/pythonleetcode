from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        nums = [0 for _ in range(10001)]
        for num, start, end in trips:
            nums[start] += num
            nums[end] -= num
        passage = 0
        for n in nums:
            passage += n
            if passage > capacity:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    print(sol.carPooling(trips, capacity))
