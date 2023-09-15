#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

class Solution:
    def search(self, arr: List[int], target: int) -> int:

        l = 0
        r = len(arr)-1
        ans = -1
        
        while l <= r:
            mid = (l+r)//2

            if arr[mid] == target:
                return mid
            
            #search for sorted half
            if arr[l] <= arr[mid]:
                if arr[l] <= target and target <= arr[mid]: # 2<=3<=4
                    r = mid -1
                else:
                    l = mid +1
            
            else:
                if target <= arr[r] and arr[mid] <= target:
                    l = mid +1
                else:
                    r = mid -1
        
        return -1
