class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
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
