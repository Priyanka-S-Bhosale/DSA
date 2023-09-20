#https://www.codingninjas.com/studio/problems/find-peak-element_1081482?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=0
def findPeakElement(arr: [int]) -> int:
    # Write your code here
    l = 1
    n = len(arr)
    r = n-2

    if n ==1: return 0

    if arr[0]>arr[1]:return 0

    if arr[n-1]>arr[n-2]: return n-1

    while l<=r:

        mid = (l+r)//2

        if arr[mid]> arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        
        elif arr[mid] >arr[mid-1]:
            l = mid+1
        
        elif arr[mid] < arr[mid+1]:
            r = mid -1
        
        else:
            l = mid+1
