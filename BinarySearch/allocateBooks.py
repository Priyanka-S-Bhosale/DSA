#https://www.codingninjas.com/studio/problems/allocate-books_1090540?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=1

def findPages(arr: [int], n: int, m: int) -> int:

    # Write your code here
    # Return the minimum number of pages
    def allocateTostudents(arr,maxPageThreshold):
        students = 1
        pagesTillNow = 0
        for i in range(len(arr)):
            if arr[i] + pagesTillNow<= maxPageThreshold:
                pagesTillNow += arr[i]
            else:
                students +=1
                pagesTillNow = arr[i]
        return students


    if len(arr)<m:
        return -1
    l = max(arr)
    r = sum(arr)

    while l <= r:
        mid = (l+r)//2
        noOfStudents = allocateTostudents(arr,mid)
        if noOfStudents > m:
            l = mid+1
        else:
            r = mid-1
    return l
