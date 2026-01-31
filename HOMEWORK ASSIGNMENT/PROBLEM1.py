# You are given an array of integers arr[]. You have to reverse the given array.
# Note: Modify the array in place. 
class Solution:
    def reverseArray(self , arc):
        # return arr(:: wrong)
        left,right=0,len(arr)-1
        while left < right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
obj = Solution()

arr=[11,4,2,7,8,3]
result=obj.reverseArray(arr)
print(result)
