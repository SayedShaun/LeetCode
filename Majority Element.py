def majorityElement(nums):
    hashMap = {}
    for i in nums:
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1

    m = max(sorted(hashMap.values()))
    for i, j in hashMap.items():
        if j == max(sorted(hashMap.values())):
            return i


nums = [3, 3, 4]
print(majorityElement(nums))
