
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        next =2
        for i in range(3,n+1):
            tmp = next
            next = prev+next
            prev = tmp
        return next
if __name__ == '__main__':
    sol=Solution()
    num=3
    print(sol.climbStairs(num))
