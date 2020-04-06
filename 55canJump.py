from typing import List
class Solution:
    #从右往前遍历
     def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        i=n-2
        if n==1:
            return True
        while i!=-1:
            if nums[i]>0:
                i-=1
                continue
            #nums[i] == 0
            for k in range(i-1,-1,-1):
                if k+nums[k]>i:
                    i=k
                    break
            else:
                return False
        return True




if __name__ == '__main__':
    sol = Solution()
    nums = [2,5,0,0]
    print(sol.canJump(nums))
