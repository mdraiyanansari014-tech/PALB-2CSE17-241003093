# Given an array arr[] with non-negative integers representing the height of blocks. 
# If the width of each block is 1, compute how much water can be trapped between 
# the blocks during the rainy season. 
class Solution():
    def trap_water(self,arr):
        if not arr:
            return 0

        left = 0
        right = len(arr) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left <= right:
            if arr[left] < arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1

        return water

obj=Solution()
arr = [2, 1, 5, 3, 1, 0, 4] 
print("Total Water Trapped =", obj.trap_water(arr))
