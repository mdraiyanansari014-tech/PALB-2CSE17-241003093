# Given an array nums with n objects colored red, white, or blue, sort them in-place so 
# that objects of the same color are adjacent, with the colors in the order red, white, and blue. 
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. 
# You must solve this problem without using the library's sort function.
#dutch flag approach will be used here
class Solution():
    def dutch_flag_approach(Self,arr):
        left=0
        mid=0
        right=len(arr)-1
        while mid<=right:
            if arr[mid]==0:
                arr[left],arr[right]=arr[mid],arr[left]
                left=left+1
                mid=mid+1

            if arr[mid]==1:
                mid=mid+1
            
            if arr[mid]==2:
                arr[mid],arr[right]=arr[right],arr[mid]
                mid=mid+1
                right=right-1
        return arr

arr=[2,0,2,1,1,0]
obj=Solution()
result=obj.dutch_flag_approach(arr)
print(arr)
