# You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position. 
# If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i. 
# If arr[i] = 0, you cannot jump forward from that position. 
# Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position. 
# Note:  Return -1 if you can't reach the end of the array.
class Solution:
    def minjumps(self,arr):
        n=len(arr)
        if arr[0]==0:
            return -1
        maximum=arr[0]
        steps=arr[0]
        jumps=1
        for i in range(1,n):
            if i == n-1:
                return jumps
            maximum=max(maximum,i+arr[i])
            steps-=1
            if steps==0:
                jumps+=1
                if i>=maximum:
                    return -1
            steps=maximum-1
        return -1




obj=Solution()
arr=[1, 3, 5, 4]
res=obj.minjumps(arr)
print(res)
