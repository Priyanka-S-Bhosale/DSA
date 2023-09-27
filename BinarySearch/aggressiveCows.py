#https://www.codingninjas.com/studio/problems/aggressive-cows_1082559?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=1

def aggressiveCows(stalls, k):
    # Write your code here.
    def placeCowsPossible(arr, distance, k):
        lastCowPlaced = arr[0]
        countCows =1
        for i in range(1, len(arr)):
            if arr[i] - lastCowPlaced >= distance:
                countCows +=1
                lastCowPlaced = arr[i]
            if countCows >= k:
                return True

        return False

    stalls.sort()
    l = 1
    n = len(stalls)
    r = stalls[n-1] - stalls[0]
    while l<=r:
        mid = (l+r)//2
        if placeCowsPossible(stalls, mid, k):
            l = mid +1
        else:
            r = mid -1
    return r


