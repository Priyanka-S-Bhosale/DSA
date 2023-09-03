#https://www.codingninjas.com/studio/problems/implement-upper-bound_8165383?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=0
def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    l =0
    r = n-1
    ans = n

    while l<=r:
        mid = (l+r)//2

        if arr[mid]>x:
            ans = mid
            r = mid-1
        else:
            l = l+1
    
    return ans

