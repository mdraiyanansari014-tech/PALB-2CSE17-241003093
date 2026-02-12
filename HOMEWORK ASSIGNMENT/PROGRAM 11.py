# Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array
import heapq
def kthsmallestelement(arr,k):
    heapq.heapify(arr) #minheap of array
    print(f"minheap array:{arr}")
    
    for _ in range(k-1):
        heapq.heappop(arr) #popping k-1 elements from heap

    return heapq.heappop(arr) #will return kth smallest element

arr=[100,17,36,25,19,7,3,2,1]
k=4
print(f"Normal array:{arr}")
print(f"{k}th smallest element : {kthsmallestelement(arr,k)}")
