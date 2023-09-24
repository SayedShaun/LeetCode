# def nextGreaterElement(nums1, nums2):
#     res = []
#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
#             if nums2[j] in nums1:
#                 if nums2[j] > nums2[j+1]:
#                     res.append(-1)
#                 else:
#                     res.append(nums2[j])
#     return res
#
#
#
#
# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# print(nextGreaterElement(nums1, nums2))


def nextGreaterElement(nums1, nums2):
    result = []
    for i in range(len(nums2)):
        if nums2[i] not in nums1:
            continue
        for j in range(i + 1, len(nums2)):
            if nums2[j] > nums2[i]:
                result.append(nums2[j])
            else:
                result.append(-1)
    return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))
