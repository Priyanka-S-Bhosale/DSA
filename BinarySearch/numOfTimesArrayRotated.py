#https://www.codingninjas.com/studio/problems/rotation_7449070?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=1
def findKRotation(arr : [int]) -> int:
    # Write your code here.
    l = 0
    r = len(arr) -1
    ans = float('inf')

    while l<=r:
        mid = (l+r)//2

        if arr[l] <= arr[mid]:
            ans = min(ans,arr[l])
            l = mid+1
        else:
            ans = min(ans,arr[mid])
            r = mid -1
    if ans == float('inf'):
        return 0
    else:
        return arr.index(ans)
