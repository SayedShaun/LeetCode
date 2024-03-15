def productExceptSelf(nums):
    product = [1] * len(nums)

    for i in range(1, len(nums)):
        product[i] = product[i-1] * nums[i-1]

    right = 1
    for j in range(len(nums) - 1, -1, -1):
        product[j] *= right
        right *= nums[j]

    return product

nums = [-1,1,0,-3,3]

result = productExceptSelf(nums)
print(result)