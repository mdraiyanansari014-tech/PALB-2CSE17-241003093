# Given an array arr and a number k. One can apply a swap operation on the array any 
# number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find 
# the minimum number of swaps required to bring all the numbers less than or equal 
# to k together, i.e. make them a contiguous subarray. 
class Solution():
    def min_swaps(Self,arr, k):
        n = len(arr)

        # Step 1: Count elements <= k
        count = 0
        for num in arr:
            if num <= k:
                count += 1

        # Step 2: Count bad elements in first window
        bad = 0
        for i in range(count):
            if arr[i] > k:
                bad += 1

        ans = bad

        # Step 3: Slide the window
        for i in range(count, n):
            # Remove element going out
            if arr[i - count] > k:
                bad -= 1

            # Add new element
            if arr[i] > k:
                bad += 1

            ans = min(ans, bad)

        return ans

obj=Solution()
arr = [2, 1, 5, 6, 3]
k = 3
result=obj.min_swaps(arr,k)
print("Minimum swaps required =", result)
