from typing import List
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        record_effc = sorted(zip(efficiency, speed), key=lambda x: (-x[0], x[1]))
        heap = []
        res = 0
        sumnum = 0
        for i in range(n):
            if len(heap) >= k:  # 保持容量为k-1个
                sumnum -= heapq.heappop(heap)
            res = max(res, (sumnum + record_effc[i][1]) * record_effc[i][0])
            heapq.heappush(heap, record_effc[i][1])
            sumnum += record_effc[i][1]
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2))
    print(sol.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3))
    print(sol.maxPerformance(n=3, speed=[2, 8, 2], efficiency=[2, 7, 1], k=2))
