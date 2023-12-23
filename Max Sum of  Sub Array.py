def maxSubArray(nums):
    curr_sum = nums[0]
    max_sum = curr_sum

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum


arr = [1, 2, 3, -4]
print(maxSubArray(arr))
