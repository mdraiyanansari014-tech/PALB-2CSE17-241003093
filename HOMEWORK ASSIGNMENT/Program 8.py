#  Given a sorted array of distinct integers and a target value, return the index if the 
# target is found. If not, return the index where it would be if it were inserted in order
class Solution:
    def returnindex(self,arr,target):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
                

obj=Solution()
arr =[3,6,8,9,11]
target=1
res=obj.returnindex(arr,target)        
print(res)
