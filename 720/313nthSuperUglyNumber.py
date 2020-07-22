from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        num = len(primes)
        count = [0] * num
        record = [1]
        res = {1}
        i = 1
        while i < n:
            curr_min, index = min(zip((record[count[i]] * primes[i] for i in range(num)), range(num)))
            count[index] += 1
            if curr_min not in res:
                record.append(curr_min)
                res.add(curr_min)
                i += 1

        print(record)
        return record[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))
