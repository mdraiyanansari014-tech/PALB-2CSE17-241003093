#  You are given an integer array arr[]. You need to find the maximum sum of a 
# subarray (containing at least one element) in the array arr[].
class Solution:
    def  maxsumsubarray(self,arr):
        maxsum = arr[0]
        currentsum = arr[0]

        for i in range(1, len(arr)):
            currentsum = max(arr[i], currentsum + arr[i])
            maxsum = max(maxsum, currentsum)
        return maxsum

obj=Solution()
arr = [2, 3, -8, 7, -1, 2, 3]
res=obj.maxsumsubarray(arr)
print(res)
