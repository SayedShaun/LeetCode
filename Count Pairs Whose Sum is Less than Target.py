def countPairs(nums, target):
    nums.sort()
    result = 0
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum < target:
            result += (right-left)
            left += 1
        else:
            right -= 1
    return result


nums = [-1, 1, 2, 3, 1]
target = 2
print(countPairs(nums, target))
