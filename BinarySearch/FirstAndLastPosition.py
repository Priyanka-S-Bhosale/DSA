#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #def binSearch(nums, target, leftBias):
        #     left = 0
        #     right = len(nums)-1
        #     index = -1
        #     while left <= right:
        #         mid = (left + right)//2
                
        #         if target > nums[mid]:
        #             left = mid +1
        #         elif target < nums[mid]:
        #             right = mid -1
        #         else:
        #             index = mid
        #             if leftBias:
        #                 right = mid -1
        #             else:
        #                 left = mid +1
        #     return index

        # left = binSearch(nums, target, True)
        # right = binSearch(nums, target, False)

        # return [left,right]
        def bs(nums, target, leftBias):
            index = -1
            l = 0
            r = len(nums) -1
            while l<=r:
                mid = (l+r)//2

                if target > nums[mid]:
                    l = mid+1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    index = mid
                    if leftBias:
                        r = mid -1
                    else:
                        l = mid +1
            return index
            
        l = bs(nums, target, True)
        r = bs(nums, target, False)
        return [l,r]
            

           
