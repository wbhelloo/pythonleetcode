from typing import List
from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """通过"""
        num = len(key)
        len_ring = len(ring)
        record = defaultdict(list)
        record_res = dict()
        for i, r in enumerate(ring):
            record[r].append(i)

        def helper(start, ring_index):
            if start == num:
                return 0
            if (start, ring_index) not in record_res.keys():
                res = float('inf')
                for index in record[key[start]]:
                    left = helper(start + 1, index) + (index - ring_index) % len_ring + 1
                    right = helper(start + 1, index) + (ring_index - index) % len_ring + 1
                    res = min(res, left, right)
                record_res[(start, ring_index)] = res
            return record_res[(start, ring_index)]

        return helper(0, 0)

    def findRotateStepsDFS(self, ring: str, key: str) -> int:
        """超时 48/340"""
        res = float('inf')
        num = len(key)
        len_ring = len(ring)
        record = defaultdict(list)
        record_res = dict()
        for i, r in enumerate(ring):
            record[r].append(i)

        def helper(start, ring_index, curr):
            nonlocal ring, res
            if curr >= res:
                return
            if start >= num:
                res = min(res, curr)
                return
            for index in record[key[start]]:
                helper(start + 1, index, curr + (index - ring_index) % len_ring + 1)
                helper(start + 1, index, curr + (ring_index - index) % len_ring + 1)

        helper(0, 0, 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findRotateSteps(ring="godding", key="godding"))
    # print(sol.findRotateSteps(ring="godding", key="gd"))
    # print(sol.findRotateSteps(ring="abcde", key="ade"))
    print(sol.findRotateSteps(ring="ababcab", key="acbaacba"))
    print(sol.findRotateStepsDFS(ring="ababcab", key="acbaacba"))
