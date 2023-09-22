#https://www.codingninjas.com/studio/problems/square-root-integral_893351?leftPanelTab=0?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries
def floorSqrt(n):
   # write your code logic here .
   l = 0
   r = n-1
   ans = 0
   
   while l<=r:
      mid = (l+r)//2

      if mid*mid <= n:
         l = mid+1
      else:
         r = mid -1

   return r

n= int(input())
print(floorSqrt(n))
