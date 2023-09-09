#https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        #take 2 different arrays one including 1st element, one including last elemet and apply house robber1 algo on it
        def houseRobber1(nums):
            
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
        
        arr1 = []
        arr2 = []

        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n):
            if i !=0:
                arr1.append(nums[i])
            if i!= n-1:
                arr2.append(nums[i])

        return max(houseRobber1(arr1),houseRobber1(arr2))
