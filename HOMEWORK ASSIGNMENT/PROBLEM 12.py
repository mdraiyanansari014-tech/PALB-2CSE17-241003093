# Given an array arr[] denoting heights of n towers and a positive integer k.
# For each tower, you must perform exactly one of the following operations exactly once.
# Increase the height of the tower by k
# Decrease the height of the tower by k
# Find out the minimum possible difference between the height of the shortest and tallest towers
# after you have modified each tower.
# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by k for each tower. After the operation,
# the resultant array should not contain any negative integers.
def mindiff(arr,k):
    n=len(arr)
    arr.sort() #sorted array
    result=arr[-1]-arr[0]

    #inc or dec in tower by k
    small=arr[0]+k
    tall=arr[n-1]-k
    
    #avoiding small<=tall
    if (small>tall):
        small,tall=tall,small
        
    for i in range(1,n):
        subtract=arr[i]-k
        add=arr[i]+k
        if subtract<0:
            continue
        new_min=min(small,subtract)
        new_max=max(tall,add)
        result=min(result,new_max-new_min)
    return result
k=2
arr=[1,3,5,8,10]
print(f"minimum possible difference between smallest and tallest tower:{mindiff(arr,k)}")
