def removeElement(nums, val):
    count = 0
    for index in nums:
        if index != val:
            nums[count] = index
            count += 1
    return count


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
