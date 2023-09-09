#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        #recursion
        # def f(index,nums):
        #     if index == 0:
        #         return nums[0]
        #     if index < 0:
        #         return 0

        #     pick = nums[index] + f(index-2, nums)
        #     notPick = 0 + f(index -1, nums)

        #     return max(pick, notPick)

        # return f(len(nums)-1, nums)

        #memoization
        # def f(dp,index,nums):
        #     if index == 0:
        #         return nums[0]
        #     if index < 0:
        #         return 0
        #     if dp[index] != -1:
        #         return dp[index]
        #     pick = nums[index] + f(dp,index-2, nums)
        #     notPick = 0 + f(dp,index -1, nums)
        #     dp[index] = max(pick, notPick)

        #     return dp[index]
        # dp = [-1]*(len(nums)+1)
        # return f(dp,len(nums)-1, nums)

        #tabulation
        # dp = [0]*(len(nums))
        # dp[0] = nums[0]
        # negative = 0
        # for index in range(1,len(nums)):
        #     pick = nums[index]
        #     if index >1:
        #         pick += dp[index-2]
        #     notPick = 0 + dp[index -1]
        #     dp[index] = max(pick, notPick)
        # return dp[len(nums)-1]


        #memory optimization

        prev = nums[0]
        prev2 = 0
        for index in range(1,len(nums)):
            pick = nums[index]
            if index >1:
                pick += prev2
            notPick = 0 + prev
            curr = max(pick, notPick)
            prev2 = prev
            prev = curr
        return prev
    
