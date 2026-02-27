# You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the 
# array is sorted in non-decreasing order. Your task is to find and return the index of the 
# first row that contains the maximum number of 1s. If no such row exists, return -1.
class Solution:
    def row_with_max_1s(self, arr):
        if not arr or not arr[0]:
            return -1

        n = len(arr)
        m = len(arr[0])

        row = 0
        col = m - 1

        max_row = -1

        while row < n and col >= 0:
            if arr[row][col] == 1:
                max_row = row
                col -= 1   # move left
            else:
                row += 1   # move down

        return max_row
obj=Solution()
arr= [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]] 
result=obj.row_with_max_1s(arr)
print(result)
