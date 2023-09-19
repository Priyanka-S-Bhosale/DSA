#https://www.codingninjas.com/studio/problems/unique-element-in-sorted-array_1112654?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=1
def singleNonDuplicate(arr):
    # Write your code here
    l = 1
    n = len(arr)
    r = n-2

    if n == 1:
        return arr[0]
    elif arr[0] != arr[1]:return arr[0]
    elif arr[n-1] != arr[n-2]: return arr[n-1]

    while l<=r:
        mid = (l+r)//2

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        elif mid%2 == 1 and arr[mid] == arr[mid-1] or mid%2==0 and arr[mid] == arr[mid+1]:
            l = mid +1 #eliminate left half
        else:
            r = mid -1
        
