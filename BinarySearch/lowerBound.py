def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    l = 0
    r = n-1
    ans = n
    while l<=r:
        mid = (l+r)//2

        if arr[mid]>=x:
            ans = mid
            r = mid -1
        else:
            l = mid +1
    return ans
