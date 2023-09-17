#https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def f(i,prev_index):
        #     if i == len(nums):
        #         return 0
        #     notPick = 0 + f(i+1, prev_index)
        #     pick = 0
        #     if prev_index == -1 or nums[i] > nums[prev_index]:
        #         pick = 1 + f(i+1,i)
            
        #     return max(pick,notPick)

        # return f(0,-1)

        #memoize

        # def f(i,prev_index,dp):
        #     if i == len(nums):
        #         return 0
        #     if dp[i][prev_index]:
        #         return dp[i][prev_index]
        #     notPick = 0 + f(i+1, prev_index,dp)
        #     pick = 0
        #     if prev_index == -1 or nums[i] > nums[prev_index]:
        #         pick = 1 + f(i+1,i,dp)
        #     dp[i][prev_index] = max(pick,notPick)
        #     return dp[i][prev_index]
        # n = len(nums)
        # dp = [[0]*(n+1) for _ in range (n+1)]
        # return f(0,-1,dp)

        #bottom up

        arr = []
        arr.append(nums[0])
        length = 1

        for i in range(1,len(nums)):
            if(nums[i]>arr[-1]):
                arr.append(nums[i])#append any element greater then last element of arr
                length+=1
                
            else:#replacing the immediate next with the smaller element
                for k in range(len(arr)):
                    if(arr[k]>=nums[i]):
                        arr[k]=nums[i]
                        break
        return length


        
        
