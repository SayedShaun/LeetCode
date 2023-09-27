def removeDuplicates(nums):
    i = 0
    while i < len(nums) - 2:
        if nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
            nums.pop(i + 2)
        else:
            i += 1
    return nums


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums))
