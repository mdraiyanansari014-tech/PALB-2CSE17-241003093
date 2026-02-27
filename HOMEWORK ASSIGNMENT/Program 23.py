# Given a number x and an array of integers arr, find the smallest subarray with sum 
# greater than the given value. If such a subarray do not exist return 0 in that case. 
class Solution:
    def smallest_subarray(self,arr, x):
        n = len(arr)
        min_length = float('inf')
        current_sum = 0
        start = 0

        for end in range(n):
            current_sum += arr[end]

            while current_sum > x:
                min_length = min(min_length, end - start + 1)
                current_sum -= arr[start]
                start += 1

        return 0 if min_length == float('inf') else min_length

obj=Solution()
arr = [1, 4, 45, 6, 0, 19]
x = 51
print("Smallest subarray length =", obj.smallest_subarray(arr, x))
