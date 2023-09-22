#https://www.codingninjas.com/studio/problems/nth-root-of-m_1062679?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries

def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here

    def multiply(mid,n):
        ans = 1
        for i in range(n):
            ans *= mid
        return ans
   
    l = 0
    r = m-1


    while l<=r:
        mid = (l+r)//2
        mult = multiply(mid,n)
        if mult == m:
            return mid
        if mult < m:
            l = mid+1
        else:
            r = mid -1

    return -1
