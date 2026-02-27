# Given an array arr[] of integers, calculate the median.
class solution:
    def median(self,arr):
        n=len(arr)
        arr.sort()
        if(n%2==1):
            return n//2
        else:
            return (arr[n//2-1]-arr[n//2])//2
obj=solution()
arr=[90,100,78,89]
result=obj.median(arr)
print(result)
