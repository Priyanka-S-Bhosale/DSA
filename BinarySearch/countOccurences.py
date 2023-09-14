#https://www.codingninjas.com/studio/problems/occurrence-of-x-in-a-sorted-array_630456?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=0
def count(arr: [int], n: int, k: int) -> int:
    def bs(arr,k,n,leftBias):
        l =0
        r = n-1
        index = -1

        while l<=r:
            mid = (l+r)//2

            if arr[mid] < k:
                l = mid+1
            elif arr[mid] >k:
                r = mid -1
            else:
                index = mid
                if leftBias:
                    r = mid-1
                else:
                    l = l+1
        return index
        
    left = bs(arr,k,n,True)
    right = bs(arr,k,n,False)
    if left == -1 and right ==-1:
        return 0
    else:
        return right - left +1 
