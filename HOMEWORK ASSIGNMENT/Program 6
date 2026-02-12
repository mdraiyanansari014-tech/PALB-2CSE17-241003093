#  Given an array arr, rotate the array by one position in clockwise direction. 
class Solution:
    def rotatearray(self,arr):
        last = arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]

        arr[0] = last
        return arr

obj=Solution()
arr = [1, 2, 3, 4, 5] 
res=obj.rotatearray(arr)
print(res)
