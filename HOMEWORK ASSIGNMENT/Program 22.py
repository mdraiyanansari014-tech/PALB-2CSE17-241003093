# Given an array arr[] of positive integers, where each value represents the number of 
# chocolates in a packet. Each packet can have a variable number of chocolates. There 
# are m students, the task is to distribute chocolate packets among m students such that - 
#       i. Each student gets exactly one packet. 
#      ii. The difference between maximum number of chocolates given to a student and 
# minimum number of chocolates given to a student is minimum and return that 
# minimum possible difference. 
class Solution():
    def min_chocolate_difference(Self,arr, m):
        n = len(arr)

        if m == 0 or n == 0:
            return 0

        if m > n:
            return -1   # Not enough packets

        arr.sort()

        min_diff = float('inf')

        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)

        return min_diff

obj=Solution()
arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print("Minimum difference =", obj.min_chocolate_difference(arr, m))
