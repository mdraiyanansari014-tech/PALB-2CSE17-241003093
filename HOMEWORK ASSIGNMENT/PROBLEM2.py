#  Given an array arr[]. Your task is to find the minimum and maximum elements in the array
arr=[1,4,2,7,2]
class Solution:
    def getMinMax(self, arr):
        max=0
        min=arr[0]
        
        l=[]
        for i in arr:
            if min>i: min=i
        l.append(min)
        for i in arr:
            if max<i: max=i
        l.append(max)
        return l
print(Solution().getMinMax(arr))
