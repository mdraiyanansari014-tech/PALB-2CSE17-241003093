# You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position. 
# If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i. 
# If arr[i] = 0, you cannot jump forward from that position. 
# Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1

        maxReach = arr[0]
        steps = arr[0]
        jumps = 1

        for i in range(1, n):
            if i == n - 1:
                return jumps
            maxReach = max(maxReach, i + arr[i])
            steps -= 1
            if steps == 0:
                jumps += 1
                if i >= maxReach:
                    return -1
                steps = maxReach - i

        return -1
obj=Solution()
arr= [1, 4, 3, 2, 6, 7] 
res=obj.minJumps(arr)
print(res)
